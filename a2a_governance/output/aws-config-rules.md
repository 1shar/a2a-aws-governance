# AWS Config Rules Documentation

## Summary of Rules

| Rule ID | Rule Name | Description |
|---|---|---|
| AWS-01 | root-mfa-check | AWS 계정 루트 사용자에 대해 다중 인증(MFA)이 활성화되어 있는지 확인합니다. |
| AWS-04 | iam-user-access-key-check | IAM 사용자의 액세스 키가 지정된 일 수(기본값 90일) 내에 교체되었는지 확인합니다. |
| AWS-05 | iam-password-policy-check | IAM 사용자에 대한 계정 암호 정책이 지정된 요구 사항을 충족하는지 확인합니다. |
| AWS-29 | s3-bucket-public-access-prohibited | S3 버킷이 공개 읽기/쓰기 액세스를 허용하지 않는지 확인합니다. |
| AWS-30 | s3-bucket-logging-enabled | S3 버킷에 로깅이 활성화되어 있는지 확인합니다. |
| AWS-32 | encrypted-volumes | EC2 인스턴스에 연결된 EBS 볼륨이 암호화되어 있는지 확인합니다. |
| AWS-33 | rds-storage-encrypted | RDS DB 인스턴스에 대해 스토리지 암호화가 활성화되어 있는지 확인합니다. |
| AWS-34 | rds-snapshots-public-prohibited | RDS 스냅샷이 공개되어 있는지 확인합니다. |
| AWS-35 | rds-instance-public-access-check | RDS DB 인스턴스가 공개적으로 액세스 가능한지 확인합니다. |


---

## Rule Details


### AWS-01-root-mfa-check

**Description**
> AWS 계정 루트 사용자에 대해 다중 인증(MFA)이 활성화되어 있는지 확인합니다.

**Rationale**
> 루트 사용자에 대해 MFA를 활성화하는 것은 매우 중요한 보안 모범 사례입니다. 루트 사용자는 AWS 계정의 모든 리소스에 대한 무제한 액세스 권한을 가집니다. MFA는 두 번째 형태의 인증을 요구하여 보안 계층을 추가하므로, 권한 없는 사용자가 암호를 알고 있더라도 계정에 액세스하기가 훨씬 더 어려워집니다.

**Remediation**
> 루트 사용자에 대해 MFA를 활성화하려면 [AWS 설명서](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-mfa)의 지침을 따르십시오.

---

### AWS-04-iam-user-access-key-check

**Description**
> IAM 사용자의 액세스 키가 지정된 일 수(기본값 90일) 내에 교체되었는지 확인합니다.

**Rationale**
> 액세스 키를 정기적으로 교체하는 것은 보안 모범 사례입니다. 이는 액세스 키가 손상되어 무단 액세스에 사용될 위험을 줄여줍니다. 액세스 키가 유출된 경우, 이를 교체하면 이전 키가 무효화되어 사용을 방지할 수 있습니다.

**Remediation**
> IAM 사용자 액세스 키를 정기적으로 교체하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey)를 참조하십시오.

---

### AWS-05-iam-password-policy-check

**Description**
> IAM 사용자에 대한 계정 암호 정책이 지정된 요구 사항을 충족하는지 확인합니다.

**Rationale**
> 강력한 암호 정책은 사용자가 추측하거나 해독하기 어려운 강력한 암호를 만들도록 보장하는 데 도움이 됩니다. 이는 AWS 계정에 대한 무단 액세스 위험을 줄입니다.

**Remediation**
> AWS 계정에 대한 강력한 암호 정책을 설정하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)를 참조하십시오.

---

### AWS-29-s3-bucket-public-access-prohibited

**Description**
> S3 버킷이 공개 읽기/쓰기 액세스를 허용하지 않는지 확인합니다.

**Rationale**
> 대중과 공유할 의도가 없는 S3 버킷은 공개해서는 안 됩니다. 이렇게 하면 권한 없는 사용자가 버킷의 데이터에 액세스하는 것을 방지할 수 있습니다.

**Remediation**
> S3 버킷에 대한 퍼블릭 액세스 차단 설정을 활성화하십시오. 자세한 내용은 [AWS 설명서](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)를 참조하십시오.

---

### AWS-30-s3-bucket-logging-enabled

**Description**
> S3 버킷에 로깅이 활성화되어 있는지 확인합니다.

**Rationale**
> S3 버킷 로깅은 버킷에 대한 요청에 대한 가시성을 제공합니다. 이 정보는 보안 모니터링, 문제 해결 및 액세스 감사에 사용할 수 있습니다.

**Remediation**
> S3 버킷에 대해 로깅을 활성화하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html)를 참조하십시오.

---

### AWS-32-encrypted-volumes

**Description**
> EC2 인스턴스에 연결된 EBS 볼륨이 암호화되어 있는지 확인합니다.

**Rationale**
> EBS 볼륨을 암호화하면 볼륨에 저장된 데이터를 보호하는 데 도움이 됩니다. 이는 보안 모범 사례입니다.

**Remediation**
> EBS 볼륨에 대해 암호화를 활성화하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)를 참조하십시오.

---

### AWS-33-rds-storage-encrypted

**Description**
> RDS DB 인스턴스에 대해 스토리지 암호화가 활성화되어 있는지 확인합니다.

**Rationale**
> RDS DB 인스턴스를 암호화하면 인스턴스에 저장된 데이터를 보호하는 데 도움이 됩니다. 이는 보안 모범 사례입니다.

**Remediation**
> RDS DB 인스턴스에 대해 스토리지 암호화를 활성화하십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)를 참조하십시오.

---

### AWS-34-rds-snapshots-public-prohibited

**Description**
> RDS 스냅샷이 공개되어 있는지 확인합니다.

**Rationale**
> 대중과 공유할 의도가 없는 RDS 스냅샷은 공개해서는 안 됩니다. 이렇게 하면 권한 없는 사용자가 스냅샷에서 DB 인스턴스를 생성하는 것을 방지할 수 있습니다.

**Remediation**
> 대중과 공유할 의도가 없는 한 RDS 스냅샷을 공개하지 마십시오. 이 작업을 수행하는 방법에 대한 지침은 [AWS 설명서](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html)를 참조하십시오.

---

### AWS-35-rds-instance-public-access-check

**Description**
> RDS DB 인스턴스가 공개적으로 액세스 가능한지 확인합니다.

**Rationale**
> 인터넷에서 액세스할 필요가 없는 RDS DB 인스턴스는 공개적으로 액세스할 수 없어야 합니다. 이는 AWS 계정의 공격 표면을 줄입니다.

**Remediation**
> RDS DB 인스턴스를 공개적으로 액세스할 수 있도록 만들지 마십시오. 대신 배스천 호스트나 VPN을 사용하여 인스턴스에 액세스하십시오.

---
