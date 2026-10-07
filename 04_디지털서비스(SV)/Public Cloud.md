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

> 클라우드 사업자가 가상화·자동화 기반 인프라를 구축하고 불특정 다수 고객에게 서비스를 제공하는 클라우드 서비스 모델

인터넷을 통해 IT 자원을 이용하는 환경에서(Where), 
불특정 다수의 고객에게 컴퓨팅 자원을 공유·제공하기 위해(What), 
클라우드 사업자가 가상화·자동화 기반의 인프라를 구축하고 사용량에 따라 서비스를 제공하는(How)
클라우드 서비스 모델(Entity)

## 키워드

| 구분                              | 설명                                                      |
| ------------------------------- | ------------------------------------------------------- |
| 멀티테넌시<br>(Multi-Tenancy)        | 단일 물리 인프라 자원을 논리적으로 분리, 격리하여 다수 이용자(Tenant)가 공동 사용하는 구조 |
| CSP<br>(Cloud Service Provider) | 클라우드 인프라를 구축·운영하고 고객에게 서비스를 제공하는 사업자                    |
| 가상화<br>(Virtualization)         | 물리 서버·스토리지·네트워크를 논리적 자원으로 추상화하여 여러 고객에게 유연하게 할당하는 핵심 기술 |
| 탄력성<br>(Elasticity)             | 서비스 부하와 사용량에 따라 컴퓨팅 자원을 신속하게 확장·축소하여 성능과 비용을 최적화하는 특성   |
| 사용량 기반 과금<br>(Pay-as-you-go)    | 고객이 실제 사용한 컴퓨팅·스토리지·네트워크 등의 자원량을 기준으로 비용을 지불하는 방식       |

# 세부

## 기출문제 분석 및 학습 가이드
### 최근 기출문제 분석 (126회 ~ 140회 및 주요 회차)
    
- 제131회 1교시
	클라우드 컴퓨팅의 Service Model, Deployment Model(Public, Private, Hybrid)

- 제114회 4교시 / 105회 3교시
	Public Cloud, Private Cloud, Hybrid Cloud의 개념, 특징 및 배치 모델별 고려사항

- 제135회 1교시/3교시 / 134회 2교시
	Public Cloud를 핵심 인프라로 연결하는 멀티클라우드
	공공부문 SaaS 이용 가이드라인
	CSAP(클라우드 보안인증) 연계
	
### 학습 가이드

- XaaS(IaaS/PaaS/SaaS) 서비스 모델과의 매핑
- Private/Hybrid Cloud와의 비교(소유권, 통제력, TCO, 보안)
- 멀티테넌시(Multi-Tenancy) 및 Security/CSAP 고려사항
- 주요 CSP(AWS, Azure, GCP 등) 사례

---


## 1장. Public Cloud의 개요 및 주요 특징
### 1.1 Public Cloud의 정의 및 등장 배경 
(On-Premise / Private Cloud 대비)
### 1.2 Public Cloud의 5대 핵심 특징 
(XaaS 기반, On-Demand, Elasticity, Multi-Tenancy, Pay-per-use)

## 2장. Public Cloud 서비스 모델 및 주요 CSP 사례
### 2.1 Service Model 연계 
(IaaS, PaaS, SaaS)
### 2.2 주요 CSP별 대표 서비스 사례 
(AWS: EC2/S3/SQS, Google: AppEngine/Docs, MS: Azure, Naver)

## 3장. Public Cloud vs Private Cloud vs Hybrid Cloud 비교
### 3.1 배치 모델(Deployment Model) 3종 비교 
(목적, 소유권, 통제력, 보안, TCO)
### 3.2 멀티클라우드(Multi-Cloud) 및 클라우드 버스팅(Cloud Bursting) 발전 방향

## 4장. Public Cloud 도입 시 주요 고려사항 및 보안/규제 이슈
### 4.1 장점 및 한계점 (Faster Time-to-Market vs Lock-in, Multi-Tenancy 보안)
### 4.2 클라우드 보안인증(CSAP), 데이터 주권(Sovereign Cloud) 및 기술사 실전 답안 전략
