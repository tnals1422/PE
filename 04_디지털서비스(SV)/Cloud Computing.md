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

>인터넷 환경에서 가상화·자동 프로비저닝·온디맨드 방식으로 자원을 제공하는 IT리소스 제공 및 운영 모델

인터넷 기반 IT 환경에서
컴퓨팅 자원을 필요에 따라 유연하게 활용하기 위해
가상화·자동 프로비저닝·온디맨드 방식으로 자원을 제공하는
IT 리소스 제공 및 운영 모델

## 키워드

| 구분                                | 내용                                                                                      |
| --------------------------------- | --------------------------------------------------------------------------------------- |
| 온디맨드<br>(On-Demand)               | 사용자가 필요한 시점에 필요한 만큼 컴퓨팅 자원을 즉시 제공받고, 사용량에 따라 자원을 조정하는 방식                                |
| 가상화(Virtualization)               | 물리적 자원(서버·스토리지·네트워크)을 논리적으로 분리하여 여러 사용자가 효율적으로 공유하도록 하는 핵심 기술                           |
| 탄력성<br>(Elasticity)               | 서비스 부하에 따라 컴퓨팅 자원을 자동으로 확장(Scale-out)하거나 축소(Scale-in)하여 성능과 비용을 최적화하는 특성                |
| XaaS<br>(Everything as a Service) | IaaS, PaaS, SaaS, FaaS 등 인프라부터 애플리케이션, 기능 단위까지 모든 IT 구성요소를 서비스 형태(Pay-per-Use)로 제공하는 모델 |
| 사용량 기반 과금<br>(Pay-as-you-go)      |  실제 사용한 컴퓨팅 자원에 따라 비용을 지불하여 초기 인프라 구축비용과 운영비용을 절감하는 과금 방식                               |

# 세부

IT Resource, On-Demand, CSB, Utility Computing
구성요소 : User Interaction Interface, Services Catalog, System Management, Provisioning Tool, Monitoring/Metering, Servers
아키텍처 : 클러스터링-분산프로그래밍-분산스토리지-분산데이터베이스-클라우드컴퓨팅
주변기술 : 가상화, 분산처리, 오픈인터페이스, 프로비저닝, 자원유틸리티, SLA, 보안,
프라이버시 보호, 공유모델
Deployment Model 유형 : Public, Hybrid, Private Cloud
Service Model 유형 : XaaS = IaaS, PaaS, SaaS, BaaS

## 기출문제 분석 및 학습 가이드

### 최근 기출문제 분석 (126회 ~ 140회 및 주요 회차)
    
- 제140회 2교시 / 제136회 1교시
	서버리스 컴퓨팅(Serverless Computing)의 정의, 특징, 구성요소 및 도입 고려사항
- 제137회 3교시
	클라우드 컴퓨팅 서비스 유형(IaaS, PaaS, SaaS, FaaS)
- 제137회 4교시
	AIaaS(AI as a Service) 의 개념 및 특징
- 제135회 3교시 / 제135회 1교시
	멀티클라우드(Multi-Cloud) 의 개념, 필요성, 요구사항 및 주요 기술
- 제134회 1교시 / 132회 3교시
	플랫폼 엔지니어링(Platform Engineering), 클라우드 관리 플랫폼(CMP)
- 제134회 2교시 / 4교시
	공공부문 SaaS 이용 가이드라인, 클라우드 전환 사업 단계별 감리 방법
### 학습 가이드

- 책임 공유 모델(Shared Responsibility Model)
- 가상화 및 프로비저닝 메커니즘
- CSP/CMP/CSB 생태계 구조
- 클라우드 보안인증(CSAP) 및 주권 클라우드(Sovereign Cloud)를 연계하여 3단락 차별화 포인트를 구성하는 것이 고득점의 핵심 전략입니다.

## 1장. 클라우드 컴퓨팅의 개요 및 주요 특징
### 1.1 클라우드 컴퓨팅의 정의 및 온프레미스(On-Premise) 대비 등장 배경
### 1.2 클라우드 컴퓨팅의 5대 핵심 특징 (On-demand, Multi-tenancy, Elasticity, Metering, Resource Pooling)

## 2장. 클라우드 서비스 모델 (Service Model / XaaS)
### 2.1 IaaS vs PaaS vs SaaS 구조 및 책임 공유 모델 (Shared Responsibility Model)
### 2.2 차세대 서비스 모델 (FaaS / Serverless, BaaS, AIaaS, SecaaS)

## 3장. 클라우드 배치 모델 (Deployment Model) 및 차세대 아키텍처
### 3.1 Public vs Private vs Hybrid Cloud 구축 전략 및 비교
### 3.2 멀티클라우드(Multi-Cloud), 인터클라우드(Inter-Cloud) 및 클라우드 버스팅(Cloud Bursting)

## 4장. 클라우드 핵심 구성요소 및 관리 플랫폼 (CSB / CMP / CSP)
### 4.1 클라우드 아키텍처 구성요소 (User Interface, Provisioning, Metering, Hypervisor/OpenStack)
### 4.2 CSP(Service Provider), CSB(Service Brokerage), CMP(Management Platform), MSP 역할 비교

## 5장. 클라우드 전환, 보안(CSAP) 및 기술사 실전 답안 전략
### 5.1 전산실 클라우드 전환 이행 절차 및 평가 항목 (118회/134회 기출)
### 5.2 클라우드 보안인증(CSAP), 주권 클라우드(Sovereign Cloud) 
