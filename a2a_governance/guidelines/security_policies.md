1. AWS CFCT 룰을 만들거야
2. template 파일을 만들어주면되는거야 너는
3. AWS Config 규칙의 이름은 AWS-"순번"-"규칙이름" 형태로 만들어줘 예를들면
ex) "AWS-01-root-mfa-check" 이런 느낌 알지?
4. 필요한 룰은 다음과 같아, 해당 내역에 대해 만들어줘

AWS-01	큰솔 접속 계정 (Root, Sub 등) MFA 설정
AWS-02	Root Account의 사용 제한
AWS-03	Root Account의 Accesskey 사용 제한
AWS-04	Accesskey관리(키 교체주기 등)
AWS-05	계정 패스워드 정책 관리
AWS-06	IAM 사용자/그룹 Admin 권한 부여 금지
AWS-07	Role 생성 최소화(사용자 계정, 서비스 Role 등)
AWS-08	AWS Bedrock 접근 관리
AWS-09	취약한 인스턴스 설정 사용 금지
AWS-10	인스턴스 로깅 설정
AWS-11	EC2 Public IP 할당 금지
AWS-12 	가상머신 이미지 Public 설정 금지
AWS-13 	서버리스 함수 Secrets값 입력 금지
AWS-23 Security Group Rule ₴ 21
AWS-24 통신구간 암호화 설정
AWS-25 NAT 게이트웨이 연결 최소화
AWS-26 ELBV2 리스너 암호화
AWS-27 ELBV2 액세스 로그 활성화
AWS-28 객체 스토리지 암호화 설정
AWS-29 객체 스토리지 Public Access 금지
AWS-30 객체 스토리지 로깅 설정
AWS-31 블록 스토리지 Public Access 금지
AWS 32 블록 스토리지 암호화 설정
AWS-33 Database 암호화 설정
AWS-34 RDS 스냅샷 퍼블릭 금지
AWS-35 RDS Public IP ₴7|
AWS-36 Database 마이너 버전 업그레이드
AWS-37 Database 로깅 설정


5. 룰에 대한 마크다운 설명 템플릿이 맘에 안들어, 이런식으로 해줘, 그리고 가이드는 한글로 설명해줘야해
예시)
----
AWS-1 콘솔 접속 계정 (Root, Sub 등) MFA 설정
점검 내용 : Root 및 IAM 계정의 콘솔 접속 가능 계정에 대하여 MFA 설정 되어있는지 확인
보안 취약점 : 콘솔 접속시 패스워드 탈취시 AWS 서비스의 대한 계정 탈취 위협이 존재함
조치 권고 사항 : MFA 설정을 적용하여, 보안성을 높여야함
---
