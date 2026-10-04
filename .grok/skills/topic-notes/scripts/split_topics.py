#!/usr/bin/env python3
"""과목 목록의 토픽 한 줄마다 template.md 양식의 노트를 만든다."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


def repo_root(source: Path, explicit: str | None) -> Path:
    if explicit:
        root = Path(explicit).expanduser().resolve()
        if not root.is_dir():
            raise SystemExit(f"저장소 루트가 없습니다: {root}")
        return root
    result = subprocess.run(
        ["git", "-C", str(source.parent), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit("git 저장소 루트를 찾지 못했습니다.")
    return Path(result.stdout.strip())


def frequency(header: str) -> str | None:
    if re.search(r"출제빈도\s*['\"]상['\"]", header):
        return "상"
    if re.search(r"출제빈도\s*['\"]중['\"]", header):
        return "중"
    if re.search(r"출제빈도\s*['\"]하['\"]", header):
        return "하"
    if "출제예상" in header:
        return "출제예상"
    return None


def topic_filename(line: str) -> str:
    # 마크다운 링크는 보이는 글자만 남긴다. / 와 : 는 파일명에 넣지 않는다.
    name = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", line.strip())
    name = name.replace("/", "·").replace(":", " - ")
    name = re.sub(r"\s+", " ", name).strip()
    if not name or name in {".", ".."}:
        raise SystemExit(f"파일명으로 쓸 수 없는 토픽입니다: {line}")
    return name


def parse_headings(text: str) -> list[tuple[str, str | None, str, str]]:
    freq = None
    items: list[tuple[str, str | None, str, str]] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            found = frequency(line)
            if found:
                freq = found
            continue
        if freq is None:
            raise SystemExit(f"출제빈도 제목 없이 토픽이 나왔습니다: {line}")
        items.append((freq, None, line, topic_filename(line)))
    return check_items(items)


def parse_tree(text: str) -> list[tuple[str, str | None, str, str]]:
    # 예제의 가지는 칸 2, 6, 10에 있다. 마지막 갈래의 자식은 │ 대신 공백이다.
    freq = None
    category = None
    items: list[tuple[str, str | None, str, str]] = []
    for raw in text.splitlines():
        if not raw.strip() or raw.strip().startswith("```"):
            continue
        mark = re.search(r"(├──|└──)\s*(.*)$", raw.rstrip())
        if not mark:
            continue
        column = mark.start()
        if column < 2 or (column - 2) % 4 != 0:
            raise SystemExit(f"목차 들여쓰기를 읽지 못했습니다: {raw.strip()}")
        depth = (column - 2) // 4 + 1
        label = mark.group(2).strip()
        if depth == 1:
            freq = frequency(label)
            if freq is None:
                raise SystemExit(f"출제빈도를 읽지 못했습니다: {label}")
            category = None
            continue
        if freq is None:
            raise SystemExit(f"출제빈도 없이 항목이 나왔습니다: {label}")
        if depth == 2:
            category = label
            continue
        if depth == 3:
            if category is None:
                raise SystemExit(f"중간 분류 없이 토픽이 나왔습니다: {label}")
            items.append((freq, category, label, topic_filename(label)))
            continue
        raise SystemExit(f"목차는 출제빈도, 중간 분류, 토픽의 세 층입니다: {label}")
    return check_items(items)


def check_items(
    items: list[tuple[str, str | None, str, str]],
) -> list[tuple[str, str | None, str, str]]:
    if not items:
        raise SystemExit("토픽이 없습니다.")
    names = [name for _, _, _, name in items]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        raise SystemExit("파일명이 겹칩니다: " + ", ".join(duplicates))
    return items


def load_topics(text: str) -> list[tuple[str, str | None, str, str]]:
    if any(("├──" in line or "└──" in line) for line in text.splitlines()):
        return parse_tree(text)
    return parse_headings(text)


def render_category(category: str, items: list[tuple[str, str | None, str, str]]) -> str:
    lines = [f"# {category}", ""]
    current = None
    for freq, _, _, name in items:
        if freq != current:
            if current is not None:
                lines.append("")
            lines.append(f"## {freq}")
            lines.append("")
            current = freq
        lines.append(f"- [{name}](<../{name}.md>)")
    lines.append("")
    return "\n".join(lines)


def subject_dir(root: Path, source: Path) -> Path:
    match = re.match(r"^(\d+)_", source.stem)
    if not match:
        raise SystemExit("과목 파일명은 숫자_ 로 시작해야 합니다. 예: 04_디지털 서비스.md")
    prefix = match.group(1) + "_"
    matches = sorted(
        path for path in root.iterdir() if path.is_dir() and path.name.startswith(prefix)
    )
    if len(matches) != 1:
        found = ", ".join(path.name for path in matches) or "없음"
        raise SystemExit(f"'{prefix}' 과목 폴더를 하나만 찾아야 합니다. 찾은 것: {found}")
    return matches[0]


def subject_tag(folder: Path) -> str:
    match = re.match(r"^(\d+)_(.+)$", folder.name)
    if not match:
        raise SystemExit(f"과목 폴더 이름을 해석하지 못했습니다: {folder.name}")
    number, rest = match.group(1), match.group(2)
    paren = re.search(r"\(([^)]+)\)\s*$", rest)
    if paren:
        return f"{number}-{paren.group(1)}"
    suffix = rest.replace(",", "").replace(" ", "")
    return f"{number}-{suffix}"


def template_file(root: Path) -> Path:
    # Obsidian 코어 플러그인 Templates 의 folder 설정을 그대로 따른다.
    config = root / ".obsidian" / "templates.json"
    if not config.is_file():
        raise SystemExit(f"템플릿 설정이 없습니다: {config}")
    folder = json.loads(config.read_text(encoding="utf-8")).get("folder")
    if not isinstance(folder, str) or not folder.strip():
        raise SystemExit("templates.json에 folder가 없습니다.")
    path = root / folder / "template.md"
    if not path.is_file():
        raise SystemExit(f"템플릿이 없습니다: {path}")
    return path


def render(template: str, tag: str, freq: str) -> str:
    if not template.startswith("---\n"):
        raise SystemExit("template.md 앞에 프론트매터가 없습니다.")
    end = template.find("\n---", 4)
    if end < 0:
        raise SystemExit("template.md 프론트매터가 닫히지 않았습니다.")
    lines = template[4:end].split("\n")
    rest = template[end + 4 :]
    if not rest.startswith("\n"):
        rest = "\n" + rest
    out: list[str] = []
    saw_tags = False
    saw_freq = False
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("tags:"):
            saw_tags = True
            out.append("tags:")
            out.append(f"  - {tag}")
            index += 1
            while index < len(lines) and lines[index].startswith(("  - ", "\t- ")):
                index += 1
            continue
        if line.startswith("출제빈도:"):
            saw_freq = True
            out.append(f"출제빈도: {freq}")
            index += 1
            continue
        out.append(line)
        index += 1
    if not saw_tags or not saw_freq:
        raise SystemExit("template.md에 tags 또는 출제빈도 칸이 없습니다.")
    body = "---\n" + "\n".join(out) + "\n---" + rest
    if not body.endswith("\n"):
        body += "\n"
    return body


def main() -> None:
    parser = argparse.ArgumentParser(description="과목 목록을 토픽 노트로 나눈다.")
    parser.add_argument("--source", required=True, help="과목 목록 markdown 파일")
    parser.add_argument("--repo", help="저장소 루트. 생략하면 git 루트")
    parser.add_argument("--category", help="이 중간 분류의 토픽과 분류 노트만 만든다")
    parser.add_argument("--dry-run", action="store_true", help="파일을 쓰지 않고 집계만 출력")
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"과목 파일이 없습니다: {source}")
    root = repo_root(source, args.repo)
    template_path = template_file(root)

    folder = subject_dir(root, source)
    tag = subject_tag(folder)
    template = template_path.read_text(encoding="utf-8")
    items = load_topics(source.read_text(encoding="utf-8"))
    if args.category:
        matched = [item for item in items if item[1] == args.category]
        if not matched:
            found = ", ".join(sorted({item[1] for item in items if item[1]})) or "없음"
            raise SystemExit(f"중간 분류가 없습니다: {args.category}. 찾은 것: {found}")
        items = matched

    created = 0
    skipped: list[str] = []
    renamed: list[tuple[str, str]] = []
    counts = {"상": 0, "중": 0, "하": 0, "출제예상": 0}
    for freq, _category, original, name in items:
        counts[freq] += 1
        if original != name:
            renamed.append((original, name))
        path = folder / f"{name}.md"
        if path.exists():
            skipped.append(name)
            continue
        created += 1
        if not args.dry_run:
            path.write_text(render(template, tag, freq), encoding="utf-8")

    category_rows: list[tuple[str, Path, int]] = []
    seen_categories: list[str] = []
    for _freq, category, _original, _name in items:
        if category and category not in seen_categories:
            seen_categories.append(category)
    category_files = [topic_filename(category) for category in seen_categories]
    category_dups = sorted({name for name in category_files if category_files.count(name) > 1})
    if category_dups:
        raise SystemExit("분류 파일명이 겹칩니다: " + ", ".join(category_dups))
    for category in seen_categories:
        members = [item for item in items if item[1] == category]
        category_path = folder / "분류" / f"{topic_filename(category)}.md"
        if category_path.exists():
            category_rows.append(("건너뜀", category_path, len(members)))
            continue
        category_rows.append(("생성", category_path, len(members)))
        if not args.dry_run:
            category_path.parent.mkdir(parents=True, exist_ok=True)
            category_path.write_text(render_category(category, members), encoding="utf-8")

    mode = "미리보기" if args.dry_run else "완료"
    print(f"상태: {mode}")
    print(f"템플릿: {template_path}")
    print(f"폴더: {folder}")
    print(f"태그: {tag}")
    print(f"원본: {len(items)}")
    print(f"생성: {created}")
    print(f"건너뜀: {len(skipped)}")
    for freq in ("상", "중", "하", "출제예상"):
        print(f"{freq}: {counts[freq]}")
    if renamed:
        print("파일명 변경:")
        for original, name in renamed:
            print(f"- {original} -> {name}")
    else:
        print("파일명 변경: 없음")
    if skipped and len(skipped) <= 15:
        print("건너뛴 파일:")
        for name in skipped:
            print(f"- {name}")
    if category_rows:
        print(f"분류 생성: {sum(1 for state, _, _ in category_rows if state == '생성')}")
        print(f"분류 건너뜀: {sum(1 for state, _, _ in category_rows if state == '건너뜀')}")
        for state, path, count in category_rows:
            print(f"- {state} {path} ({count})")


if __name__ == "__main__":
    main()