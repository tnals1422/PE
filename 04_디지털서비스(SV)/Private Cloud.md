---
tags:
  - 04-SV
출제빈도: 상
단계:
회독: 0
마지막 확인:
기필반: 필수
---
# 핵심
## 정의

특정 조직 전용 IT 환경에서(Where), 
조직의 요구사항에 맞는 컴퓨팅 자원의 독립적 운영과 통제를 위해(What), 
가상화·자동화·클라우드 관리 기술을 적용하여 전용 자원을 제공하는(How) 
클라우드 컴퓨팅 환경(Entity)


"프라이빗 클라우드(Private Cloud)는 기업 내부의 폐쇄된 네트워크 환경에서 가상화 및 SDDC 기술을 기반으로 자체 자원 풀을 구성하여, 데이터 소유권 및 강력한 보안 통제권을 보장하는 전용 클라우드 배치 모델이다."

- Private Cloud는 기업/기관 내부의 폐쇄된 네트워크 환경(방화벽 내)에서 전용으로 구축·운용되는 독자적 클라우드 인프라입니다.

## 핵심 키워드

**핵심1 - 전용 인프라(Dedicated Infrastructure)** : 특정 조직만 사용하는 서버·스토리지·네트워크 등의 전용 자원을 구성하여 외부 고객과 물리적 또는 논리적으로 분리

**핵심2 - 보안성(Security)** : 데이터와 시스템을 조직의 통제 영역에서 운영할 수 있어 높은 수준의 보안 정책과 접근통제를 적용할 수 있음

**핵심3 - 가상화(Virtualization)** : 물리적 IT 자원을 가상 머신이나 가상 네트워크 등 논리적 자원으로 추상화하여 자원 활용도를 향상

**핵심4 - 자동화 및 오케스트레이션(Automation & Orchestration)** : 자원 프로비저닝, 배포, 모니터링 및 확장 등의 운영 작업을 자동화하여 관리 효율성을 향상

**핵심5 - 통제 및 커스터마이징(Control & Customization)** : 조직의 보안·규정·성능 요구사항에 따라 인프라 구조와 운영 정책을 세밀하게 설계하고 통제할 수 있음

- **Where (어디에서, 어떤 맥락에서 등장했는가)**:
    - 금융사, 정부기관, 대기업처럼 **데이터 보안과 개인정보보호가 최우선인 조직**에서, 외부 공용 클라우드(AWS, Azure 등)로 데이터를 보내기엔 해킹/유출 위험이 크고, 그렇다고 기존 전산실(On-Premise) 방식대로 쓰기엔 자원 효율이 떨어지는 고민에서 등장했습니다.
- **What (그것은 무엇을 하는가, 핵심 기능은 무엇인가)**:
    - 기업 자체 데이터센터 내부에 독자적인 클라우드 환경을 만들어, **내부 임직원이나 특정 전용 사용자에게만 배타적이고 안전하게 IT 자원을 빌려주는 프라이빗 클라우드 서비스**입니다.
- **How (어떤 방식으로 작동하는가, 어떤 원리인가)**:
    - 기업 내부의 서버·스토리지·네트워크를 가상화(Hypervisor, OpenStack, SDDC)하여 하나의 커다란 자원 풀(Resource Pool)로 묶은 뒤, 관리 포털(Request/Operations UI)을 통해 내부 부서가 요청하면 **셀프 서비스 프로비저닝**으로 자원을 즉시 할당하고 모니터링합니다.
- **Entity (그것의 정체는 무엇인가, 어떤 범주에 속하는가)**:
    - 기업이 인프라 소유권과 완전한 통제권을 보유하는 **기업 전용(Enterprise/Internal) 클라우드 배치 모델**입니다.


# 세부

## 기출문제 분석 및 학습 가이드

###  최근 기출문제 분석 (126회 ~ 140회 및 주요 회차)
 - 제131회 1교시
	 클라우드 컴퓨팅의 Service Model, Deployment Model(Public, Private, Hybrid)
- 제114회 4교시 / 105회 3교시
	Private Cloud, Public Cloud, Hybrid Cloud에 대한 개념, 특징 및 배치 모델별 고려사항
    - 연계 기출 토픽
	    Private Cloud의 핵심 구축 기술인 오픈스택(OpenStack), 가상화/스토리지 가상화(134회 1교시), 클라우드 전환 사업(134회 4교시) 및 주권 클라우드(Sovereign Cloud)가 연속 출제되고 있습니다.
### 학습 가이드

- On-Premise vs Private Cloud vs Public Cloud 비교
- SDDC(SDC, SDS, SDN) 및 OpenStack 기반 구축 아키텍처
- 서비스 관리 요소(Service Catalogue, Metering, Chargeback)
- 데이터 주권/보안성 확보와 초기 구축비용(CAPEX) 간의 Trade-off를 3단락 차별화 포인트로 제시하는 것이 고득점의 핵심 전략입니다.

## 1장. Private Cloud의 개요 및 주요 특징
### 1.1 Private Cloud의 정의, 등장 배경 및 On-Premise 대비 차이점
### 1.2 Private Cloud의 4대 주요 특징 (배타적 서비스, 완전 통제권, 높은 보안성, 자산 투자 필요성)

## 2장. Private Cloud의 아키텍처 및 핵심 구성요소
### 2.1 Private Cloud 통합 아키텍처 (서비스 관리 레이어 vs 가상화/물리 레이어)
### 2.2 핵심 구성요소 (Service Catalogue, Request/Operations UI, Management & Monitoring, Metering/Chargeback, Firewall/DMZ)

## 3장. Private Cloud 핵심 구축 기술 (SDDC & OpenStack)
### 3.1 SDDC(Software Defined Data Center: SDC, SDS, SDN) 기반 구축 전략
### 3.2 오픈소스 IaaS 플랫폼 OpenStack 핵심 프로젝트 (Nova, Glance, Cinder, Swift, Neutron, Horizon) 기반 구현

## 4장. Private Cloud vs Public Cloud vs Hybrid Cloud 비교
### 4.1. 3대 클라우드 배치 모델 비교 (목적, 소유권, 통제력, 보안, TCO, 유연성)
### 4.2. 하이브리드 클라우드 연계(Cloud Bursting / DRS) 및 25점 서술형 답안 차별화 전략
