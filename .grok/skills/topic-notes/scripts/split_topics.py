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


def parse_topics(text: str) -> list[tuple[str, str, str]]:
    freq = None
    items: list[tuple[str, str, str]] = []
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
        items.append((freq, line, topic_filename(line)))
    if not items:
        raise SystemExit("토픽이 없습니다.")
    names = [name for _, _, name in items]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        raise SystemExit("파일명이 겹칩니다: " + ", ".join(duplicates))
    return items


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
    items = parse_topics(source.read_text(encoding="utf-8"))

    created = 0
    skipped: list[str] = []
    renamed: list[tuple[str, str]] = []
    counts = {"상": 0, "중": 0, "하": 0, "출제예상": 0}
    for freq, original, name in items:
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


if __name__ == "__main__":
    main()