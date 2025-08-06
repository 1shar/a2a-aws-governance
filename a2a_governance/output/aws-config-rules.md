# AWS Config Rules

This document describes the AWS Config rules that are deployed to the AWS account.


## AWS-01-root-mfa-check

**Rule Description:**

AWS 계정 루트 사용자에 대해 다중 인증(MFA)이 활성화되어 있는지 확인합니다.

**Rationale:**

루트 사용자에 대해 MFA를 활성화하는 것은 매우 중요한 보안 모범 사례입니다. 루트 사용자는 AWS 계정의 모든 리소스에 대한 무제한 액세스 권한을 가집니다. MFA는 두 번째 형태의 인증을 요구하여 보안 계층을 추가하므로, 권한 없는 사용자가 암호를 알고 있더라도 계정에 액세스하기가 훨씬 더 어려워집니다.

**Remediation:**

루트 사용자에 대해 MFA를 활성화하려면 [AWS 설명서](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-mfa)의 지침을 따르십시오.


## AWS-02-root-account-usage-check

**Rule Description:**

루트 계정이 지난 24시간 동안 사용되었는지 확인합니다.

**Rationale:**

루트 계정은 일상적인 작업에 사용해서는 안 됩니다. 일상적인 운영을 위해서는 적절한 권한을 가진 IAM 사용자를 생성하여 사용하는 것이 좋습니다. 루트 계정 사용은 특별히 필요한 작업으로 제한되어야 합니다.

**Remediation:**

일상적인 작업에는 루트 계정을 사용하지 마십시오. 최소 권한 원칙에 따라 IAM 사용자를 생성하여 사용하십시오. 자세한 내용은 [AWS 설명서](https.docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#create-iam-users)를 참조하십시오.


## AWS-03-root-account-access-key-check

**Rule Description:**

루트 계정에 활성 액세스 키가 있는지 확인합니다.

**Rationale:**

액세스 키는 AWS 계정에 프로그래밍 방식의 액세스를 제공합니다. 루트 계정과 연결된 액세스 키를 두지 않는 것이 보안 모범 사례입니다. 대신 특정 권한을 가진 IAM 사용자를 만들고 해당 사용자를 위한 액세스 키를 생성하십시오.

**Remediation:**

루트 계정에 대한 액세스 키가 있는 경우 제거해야 합니다. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/IAM/latest/UserGuide/managing-root-access-keys.html)를 참조하십시오.


## AWS-04-iam-user-access-key-check

**Rule Description:**

IAM 사용자의 액세스 키가 지정된 일 수(기본값 90일) 내에 교체되었는지 확인합니다.

**Rationale:**

액세스 키를 정기적으로 교체하는 것은 보안 모범 사례입니다. 이는 액세스 키가 손상되어 무단 액세스에 사용될 위험을 줄여줍니다. 액세스 키가 유출된 경우, 이를 교체하면 이전 키가 무효화되어 사용을 방지할 수 있습니다.

**Remediation:**

IAM 사용자 액세스 키를 정기적으로 교체하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey)를 참조하십시오.


## AWS-05-iam-password-policy-check

**Rule Description:**

IAM 사용자에 대한 계정 암호 정책이 지정된 요구 사항을 충족하는지 확인합니다.

**Rationale:**

강력한 암호 정책은 사용자가 추측하거나 해독하기 어려운 강력한 암호를 만들도록 보장하는 데 도움이 됩니다. 이는 AWS 계정에 대한 무단 액세스 위험을 줄입니다.

**Remediation:**

AWS 계정에 대한 강력한 암호 정책을 설정하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)를 참조하십시오.


## AWS-06-iam-policy-no-administrative-privileges-check

**Rule Description:**

IAM 정책이 관리자 권한을 부여하지 않는지 확인합니다.

**Rationale:**

IAM 사용자 또는 그룹에 관리자 권한을 부여하는 것은 피해야 합니다. 대신 사용자 또는 그룹이 작업을 수행하는 데 필요한 권한만 부여하십시오. 이를 최소 권한의 원칙이라고 합니다.

**Remediation:**

IAM 사용자 또는 그룹에 관리자 권한을 부여하지 마십시오. 대신 필요한 권한만 부여하는 정책을 만드십시오. 자세한 내용은 [AWS 설명서](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)를 참조하십시오.


## AWS-07-iam-role-creation-minimized

**Rule Description:**

(사용자 지정 규칙) IAM 역할 생성을 최소화하고 모니터링합니다. 이 규칙은 새 역할 생성을 추적하기 위해 사용자 지정 Lambda 함수가 필요합니다.

**Rationale:**

불필요한 IAM 역할 생성을 제한하고, 생성되는 모든 역할을 검토하여 최소 권한 원칙을 준수하는지 확인해야 합니다.

**Remediation:**

새로운 IAM 역할 생성 시, 반드시 필요한 최소한의 권한만 부여하고, 생성된 역할은 정기적으로 검토 및 감사해야 합니다. CloudTrail과 Lambda를 사용하여 역할 생성을 모니터링하는 자동화된 알림을 설정하십시오.


## AWS-08-bedrock-access-management

**Rule Description:**

(사용자 지정 규칙) AWS Bedrock에 대한 접근을 관리하고 모니터링합니다. 이 규칙은 Bedrock 관련 권한 변경을 감지하기 위해 사용자 지정 Lambda 함수가 필요합니다.

**Rationale:**

AWS Bedrock과 같은 강력한 AI 서비스에 대한 접근은 엄격하게 통제되어야 하며, 승인된 사용자 및 서비스만 접근할 수 있도록 보장해야 합니다.

**Remediation:**

Bedrock 서비스에 대한 접근 권한은 IAM 정책을 통해 명시적으로 부여하고, 최소 권한 원칙에 따라 필요한 작업만 허용하도록 제한해야 합니다. IAM Access Analyzer나 사용자 지정 Lambda를 사용하여 비정상적인 접근 권한 부여를 모니터링하십시오.


## AWS-09-ec2-instance-profile-check

**Rule Description:**

EC2 인스턴스가 인스턴스 프로파일을 사용하고 있는지 확인합니다.

**Rationale:**

EC2 인스턴스는 다른 AWS 서비스에 액세스하는 데 필요한 권한을 제공하기 위해 인스턴스 프로파일로 시작해야 합니다. 이는 인스턴스에 액세스 키를 저장하는 것보다 더 안전합니다.

**Remediation:**

인스턴스 프로파일로 EC2 인스턴스를 시작하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)를 참조하십시오.


## AWS-10-instance-logging-check

**Rule Description:**

인스턴스 로깅 설정 (CloudWatch Logs 암호화)을 확인합니다.

**Rationale:**

CloudWatch 로그 그룹을 암호화하면 로그에 저장된 민감한 데이터를 보호하는 데 도움이 됩니다. 이는 보안 모범 사례입니다.

**Remediation:**

CloudWatch 로그 그룹에 대해 암호화를 활성화하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html)를 참조하십시오.


## AWS-11-ec2-no-public-ip-check

**Rule Description:**

EC2 인스턴스에 퍼블릭 IP 주소가 없는지 확인합니다.

**Rationale:**

인터넷에서 액세스할 필요가 없는 EC2 인스턴스는 퍼블릭 IP 주소를 가져서는 안 됩니다. 이는 AWS 계정의 공격 표면을 줄입니다.

**Remediation:**

인터넷에서 액세스할 필요가 없는 EC2 인스턴스에 퍼블릭 IP 주소를 할당하지 마십시오. 대신 배스천 호스트나 VPN을 사용하여 인스턴스에 액세스하십시오.


## AWS-12-ami-not-public-check

**Rule Description:**

가상머신 이미지(AMI)가 퍼블릭으로 설정되지 않았는지 확인합니다.

**Rationale:**

대중과 공유할 의도가 없는 AMI는 공개해서는 안 됩니다. 이렇게 하면 권한 없는 사용자가 AMI에서 인스턴스를 시작하는 것을 방지할 수 있습니다.

**Remediation:**

대중과 공유할 의도가 없는 한 AMI를 공개하지 마십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html)를 참조하십시오.


## AWS-13-lambda-function-no-secrets

**Rule Description:**

(사용자 지정 규칙) 서버리스 함수 코드에 Secrets 값이 직접 입력되지 않았는지 확인합니다. 이 규칙은 함수 코드를 스캔하기 위해 사용자 지정 Lambda 함수가 필요합니다.

**Rationale:**

소스 코드에 암호나 API 키와 같은 민감한 정보를 하드코딩하는 것은 심각한 보안 위험입니다. 이러한 정보는 AWS Secrets Manager나 Parameter Store와 같은 안전한 저장소를 통해 관리해야 합니다.

**Remediation:**

Lambda 함수 코드에서 하드코딩된 모든 보안 정보를 제거하고, AWS Secrets Manager 또는 Parameter Store를 사용하도록 코드를 리팩토링하십시오.


## AWS-20-vpc-network-separation

**Rule Description:**

(사용자 지정 규칙) 개발, 스테이징, 프로덕션 환경에 대한 VPC 망분리가 필요한지 확인합니다.

**Rationale:**

환경별(개발, 스테이징, 프로덕션)로 네트워크를 분리(VPC)하면, 한 환경의 보안 문제가 다른 환경으로 전파되는 것을 방지하고 각 환경에 맞는 보안 정책을 적용할 수 있습니다.

**Remediation:**

각 환경(DEV, STG, PRD)에 대해 별도의 VPC를 생성하여 네트워크를 격리하십시오. 각 VPC는 고유한 CIDR 블록을 가져야 하며, 환경 간 통신은 반드시 필요한 경우에만 VPC 피어링이나 Transit Gateway를 통해 엄격하게 제어되어야 합니다.


## AWS-21-vpc-peering-restriction

**Rule Description:**

(사용자 지정 규칙) 환경 간 VPC 피어링을 금지하는지 확인합니다.

**Rationale:**

개발, 스테이징, 프로덕션 환경 간의 무분별한 VPC 피어링은 망 분리의 목적을 무의미하게 만들고 보안 위험을 증가시킬 수 있습니다.

**Remediation:**

환경 간 VPC 피어링은 기본적으로 금지하고, 반드시 필요한 경우에만 엄격한 보안 검토 및 승인 프로세스를 거쳐 최소한의 범위로 허용해야 합니다. AWS Config 규칙을 사용하여 의도하지 않은 피어링 연결 생성을 탐지하고 알림을 받으십시오.


## AWS-22-vpc-flow-logs-enabled

**Rule Description:**

Amazon Virtual Private Cloud(VPC) 흐름 로그가 활성화되어 있는지 확인합니다.

**Rationale:**

VPC 흐름 로그는 VPC로 들어오고 나가는 트래픽에 대한 가시성을 제공합니다. 이 정보는 보안 모니터링, 문제 해결 및 네트워크 트래픽 분석에 사용할 수 있습니다.

**Remediation:**

VPC에 대해 VPC 흐름 로그를 활성화하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)를 참조하십시오.


## AWS-23-restricted-common-ports

**Rule Description:**

사용 중인 보안 그룹이 지정된 IP 주소에 대해 무제한 수신 트래픽을 허용하는지 확인합니다.

**Rationale:**

수신 트래픽을 필요한 포트 및 IP 주소로만 제한하면 AWS 계정의 공격 표면을 줄이는 데 도움이 됩니다.

**Remediation:**

필요한 포트 및 IP 주소에서만 수신 트래픽을 허용하도록 보안 그룹을 구성하십시오. 자세한 내용은 [AWS 설명서](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)를 참조하십시오.


## AWS-24-elb-custom-security-policy-ssl-check

**Rule Description:**

클래식 로드 밸런서가 사용자 지정 보안 정책을 사용하고 있는지 확인합니다.

**Rationale:**

사용자 지정 보안 정책을 사용하면 로드 밸런서가 클라이언트와 통신하는 데 사용하는 SSL/TLS 프로토콜 및 암호를 지정할 수 있습니다. 이는 애플리케이션의 보안을 개선하는 데 도움이 될 수 있습니다.

**Remediation:**

클래식 로드 밸런서가 사용자 지정 보안 정책을 사용하도록 구성하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-options.html)를 참조하십시오.


## AWS-25-nat-gateway-connection-minimization

**Rule Description:**

(사용자 지정 규칙) NAT 게이트웨이 연결을 최소화하는지 확인합니다.

**Rationale:**

NAT 게이트웨이는 프라이빗 서브넷의 인스턴스가 외부 서비스에 연결할 수 있도록 하지만, 불필요한 NAT 게이트웨이는 비용을 증가시키고 관리 복잡성을 높일 수 있습니다.

**Remediation:**

VPC 내에서 NAT 게이트웨이의 수를 최소화하고, 가능한 경우 여러 프라이빗 서브넷이 하나의 NAT 게이트웨이를 공유하도록 아키텍처를 설계하십시오. NAT 게이트웨이 사용량을 정기적으로 모니터링하고 불필요한 게이트웨이는 제거하십시오.


## AWS-26-elbv2-listener-https-only

**Rule Description:**

애플리케이션 로드 밸런서 및 네트워크 로드 밸런서 리스너가 HTTPS용으로 구성되어 있는지 확인합니다.

**Rationale:**

HTTPS를 사용하면 클라이언트와 애플리케이션 간에 전송되는 데이터를 보호하는 데 도움이 됩니다. 이는 보안 모범 사례입니다.

**Remediation:**

애플리케이션 로드 밸런서 및 네트워크 로드 밸런서 리스너를 HTTPS용으로 구성하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html)를 참조하십시오.


## AWS-27-elbv2-access-logs-enabled

**Rule Description:**

애플리케이션 로드 밸런서 및 네트워크 로드 밸런서에 액세스 로깅이 활성화되어 있는지 확인합니다.

**Rationale:**

액세스 로그는 로드 밸런서를 통과하는 트래픽에 대한 가시성을 제공합니다. 이 정보는 보안 모니터링, 문제 해결 및 트래픽 분석에 사용할 수 있습니다.

**Remediation:**

애플리케이션 로드 밸런서 및 네트워크 로드 밸런서에 대해 액세스 로깅을 활성화하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html)를 참조하십시오.


## AWS-28-s3-bucket-server-side-encryption-enabled

**Rule Description:**

S3 버킷에 서버 측 암호화가 활성화되어 있는지 확인합니다.

**Rationale:**

서버 측 암호화는 S3 버킷에 저장된 데이터를 보호하는 데 도움이 됩니다. 이는 보안 모범 사례입니다.

**Remediation:**

S3 버킷에 대해 서버 측 암호화를 활성화하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html)를 참조하십시오.


## AWS-29-s3-bucket-public-access-prohibited

**Rule Description:**

S3 버킷이 공개 읽기/쓰기 액세스를 허용하지 않는지 확인합니다.

**Rationale:**

대중과 공유할 의도가 없는 S3 버킷은 공개해서는 안 됩니다. 이렇게 하면 권한 없는 사용자가 버킷의 데이터에 액세스하는 것을 방지할 수 있습니다.

**Remediation:**

S3 버킷에 대한 퍼블릭 액세스 차단 설정을 활성화하십시오. 자세한 내용은 [AWS 설명서](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)를 참조하십시오.


## AWS-30-s3-bucket-logging-enabled

**Rule Description:**

S3 버킷에 로깅이 활성화되어 있는지 확인합니다.

**Rationale:**

S3 버킷 로깅은 버킷에 대한 요청에 대한 가시성을 제공합니다. 이 정보는 보안 모니터링, 문제 해결 및 액세스 감사에 사용할 수 있습니다.

**Remediation:**

S3 버킷에 대해 로깅을 활성화하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html)를 참조하십시오.


## AWS-31-ebs-snapshot-public-restorable-check

**Rule Description:**

EBS 스냅샷이 공개적으로 복원 가능하지 않은지 확인합니다.

**Rationale:**

대중과 공유할 의도가 없는 EBS 스냅샷은 공개해서는 안 됩니다. 이렇게 하면 권한 없는 사용자가 스냅샷에서 볼륨을 생성하는 것을 방지할 수 있습니다.

**Remediation:**

대중과 공유할 의도가 없는 한 EBS 스냅샷을 공개하지 마십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html)를 참조하십시오.


## AWS-32-encrypted-volumes

**Rule Description:**

EC2 인스턴스에 연결된 EBS 볼륨이 암호화되어 있는지 확인합니다.

**Rationale:**

EBS 볼륨을 암호화하면 볼륨에 저장된 데이터를 보호하는 데 도움이 됩니다. 이는 보안 모범 사례입니다.

**Remediation:**

EBS 볼륨에 대해 암호화를 활성화하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)를 참조하십시오.


## AWS-33-rds-storage-encrypted

**Rule Description:**

RDS DB 인스턴스에 대해 스토리지 암호화가 활성화되어 있는지 확인합니다.

**Rationale:**

RDS DB 인스턴스를 암호화하면 인스턴스에 저장된 데이터를 보호하는 데 도움이 됩니다. 이는 보안 모범 사례입니다.

**Remediation:**

RDS DB 인스턴스에 대해 스토리지 암호화를 활성화하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)를 참조하십시오.


## AWS-34-rds-snapshots-public-prohibited

**Rule Description:**

RDS 스냅샷이 공개되어 있는지 확인합니다.

**Rationale:**

대중과 공유할 의도가 없는 RDS 스냅샷은 공개해서는 안 됩니다. 이렇게 하면 권한 없는 사용자가 스냅샷에서 DB 인스턴스를 생성하는 것을 방지할 수 있습니다.

**Remediation:**

대중과 공유할 의도가 없는 한 RDS 스냅샷을 공개하지 마십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html)를 참조하십시오.


## AWS-35-rds-instance-public-access-check

**Rule Description:**

RDS DB 인스턴스가 공개적으로 액세스 가능한지 확인합니다.

**Rationale:**

인터넷에서 액세스할 필요가 없는 RDS DB 인스턴스는 공개적으로 액세스할 수 없어야 합니다. 이는 AWS 계정의 공격 표면을 줄입니다.

**Remediation:**

RDS DB 인스턴스를 공개적으로 액세스할 수 있도록 만들지 마십시오. 대신 배스천 호스트나 VPN을 사용하여 인스턴스에 액세스하십시오.


## AWS-36-rds-minor-version-upgrade-enabled

**Rule Description:**

RDS DB 인스턴스에 부 버전 업그레이드가 활성화되어 있는지 확인합니다.

**Rationale:**

부 버전 업그레이드를 활성화하면 RDS DB 인스턴스가 최신 보안 패치 및 버그 수정을 실행하고 있는지 확인하는 데 도움이 됩니다.

**Remediation:**

RDS DB 인스턴스에 대해 부 버전 업그레이드를 활성화하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MinorVersionUpgrade.html)를 참조하십시오.


## AWS-37-rds-logging-enabled

**Rule Description:**

RDS DB 인스턴스에 로깅이 활성화되어 있는지 확인합니다.

**Rationale:**

RDS 로깅은 DB 인스턴스의 활동에 대한 가시성을 제공합니다. 이 정보는 보안 모니터링, 문제 해결 및 성능 분석에 사용할 수 있습니다.

**Remediation:**

RDS DB 인스턴스에 대해 로깅을 활성화하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html)를 참조하십시오.

