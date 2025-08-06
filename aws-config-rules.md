# AWS Config Rules

This document describes the AWS Config rules that are deployed to the AWS account.

## AWS-01-root-mfa-check

**Rule Description:**

This rule checks whether the AWS account root user has multi-factor authentication (MFA) enabled.

**Rationale:**

Enabling MFA for the root user is a critical security best practice. The root user has unrestricted access to all resources in the AWS account. MFA adds an extra layer of security by requiring a second form of authentication, making it much more difficult for unauthorized users to gain access to the account, even if they have the password.

**Remediation:**

To enable MFA for the root user, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-mfa).

## AWS-02-root-account-usage-check

**Rule Description:**

This rule checks whether the root account has been used in the last 24 hours.

**Rationale:**

The root account should not be used for routine tasks. It is recommended to create IAM users with appropriate permissions for daily operations. Using the root account should be limited to tasks that specifically require it.

**Remediation:**

Avoid using the root account for everyday tasks. Create and use IAM users with the principle of least privilege. For more information, see the [AWS documentation](https.docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#create-iam-users).

## AWS-03-root-account-access-key-check

**Rule Description:**

This rule checks whether the root account has active access keys.

**Rationale:**

Access keys provide programmatic access to your AWS account. It is a security best practice to not have access keys associated with the root account. Instead, create IAM users with specific permissions and generate access keys for those users.

**Remediation:**

If there are access keys for the root account, they should be removed. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/managing-root-access-keys.html).

## AWS-04-iam-user-access-key-check

**Rule Description:**

This rule checks whether IAM users have access keys that have been rotated within the specified number of days (default is 90 days).

**Rationale:**

Regularly rotating access keys is a security best practice. It reduces the risk of an access key being compromised and used for unauthorized access. If an access key is leaked, rotating it will invalidate the old key and prevent it from being used.

**Remediation:**

Rotate IAM user access keys on a regular basis. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey).

## AWS-05-iam-password-policy-check

**Rule Description:**

This rule checks whether the account password policy for IAM users meets the specified requirements.

**Rationale:**

A strong password policy helps to ensure that users create strong passwords that are difficult to guess or crack. This reduces the risk of unauthorized access to your AWS account.

**Remediation:**

Set a strong password policy for your AWS account. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html).

## AWS-06-iam-policy-no-administrative-privileges-check

**Rule Description:**

This rule checks that no IAM policies grant administrative privileges.

**Rationale:**

Granting administrative privileges to IAM users or groups should be avoided. Instead, grant only the permissions that are required for the user or group to perform their tasks. This is known as the principle of least privilege.

**Remediation:**

Do not grant administrative privileges to IAM users or groups. Instead, create policies that grant only the necessary permissions. For more information, see the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege).

## AWS-09-ec2-instance-profile-check

**Rule Description:**

This rule checks whether your EC2 instances are using an instance profile.

**Rationale:**

EC2 instances should be launched with an instance profile to provide them with the necessary permissions to access other AWS services. This is more secure than storing access keys on the instance.

**Remediation:**

Launch EC2 instances with an instance profile. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html).

## AWS-10-cloudwatch-log-group-encrypted-check

**Rule Description:**

This rule checks whether CloudWatch log groups are encrypted.

**Rationale:**

Encrypting CloudWatch log groups helps to protect sensitive data that is stored in logs. This is a security best practice.

**Remediation:**

Enable encryption for your CloudWatch log groups. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html).

## AWS-11-ec2-no-public-ip-check

**Rule Description:**

This rule checks that EC2 instances do not have public IP addresses.

**Rationale:**

EC2 instances that do not need to be accessed from the internet should not have public IP addresses. This reduces the attack surface of your AWS account.

**Remediation:**

Do not assign public IP addresses to EC2 instances that do not need to be accessed from the internet. Instead, use a bastion host or a VPN to access the instances.

## AWS-12-ami-not-public-check

**Rule Description:**

This rule checks that AMIs are not public.

**Rationale:**

AMIs that are not intended to be shared with the public should not be made public. This prevents unauthorized users from launching instances from your AMIs.

**Remediation:**

Do not make AMIs public unless they are intended to be shared with the public. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html).

## AWS-22-vpc-flow-logs-enabled

**Rule Description:**

This rule checks whether Amazon Virtual Private Cloud (VPC) flow logs are enabled.

**Rationale:**

VPC flow logs provide visibility into the traffic that is flowing into and out of your VPC. This information can be used for security monitoring, troubleshooting, and network traffic analysis.

**Remediation:**

Enable VPC flow logs for your VPCs. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html).

## AWS-23-restricted-incoming-traffic

**Rule Description:**

This rule checks whether security groups that are in use allow unrestricted incoming traffic.

**Rationale:**

Restricting incoming traffic to only the necessary ports and IP addresses helps to reduce the attack surface of your AWS account.

**Remediation:**

Configure your security groups to allow incoming traffic from only the necessary ports and IP addresses. For more information, see the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html).

## AWS-24-elb-custom-security-policy-ssl-check

**Rule Description:**

This rule checks whether your Classic Load Balancer is using a custom security policy.

**Rationale:**

Using a custom security policy allows you to specify the SSL/TLS protocols and ciphers that your load balancer uses to communicate with clients. This can help to improve the security of your application.

**Remediation:**

Configure your Classic Load Balancer to use a custom security policy. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-options.html).

## AWS-26-elbv2-listener-https-only

**Rule Description:**

This rule checks whether your Application Load Balancer and Network Load Balancer listeners are configured for HTTPS.

**Rationale:**

Using HTTPS helps to protect the data that is transmitted between your clients and your application. This is a security best practice.

**Remediation:**

Configure your Application Load Balancer and Network Load Balancer listeners for HTTPS. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html).

## AWS-27-elbv2-access-logs-enabled

**Rule Description:**

This rule checks whether your Application Load Balancer and Network Load Balancer have access logging enabled.

**Rationale:**

Access logs provide visibility into the traffic that is flowing through your load balancers. This information can be used for security monitoring, troubleshooting, and traffic analysis.

**Remediation:**

Enable access logging for your Application Load Balancers and Network Load Balancers. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html).

## AWS-28-s3-bucket-server-side-encryption-enabled

**Rule Description:**

This rule checks that your S3 buckets have server-side encryption enabled.

**Rationale:**

Server-side encryption helps to protect the data that is stored in your S3 buckets. This is a security best practice.

**Remediation:**

Enable server-side encryption for your S3 buckets. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html).

## AWS-29-s3-bucket-public-access-prohibited

**Rule Description:**

This rule checks that your S3 buckets do not allow public access.

**Rationale:**

S3 buckets that are not intended to be shared with the public should not be made public. This prevents unauthorized users from accessing the data in your buckets.

**Remediation:**

Do not make S3 buckets public unless they are intended to be shared with the public. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html).

## AWS-30-s3-bucket-logging-enabled

**Rule Description:**

This rule checks that your S3 buckets have logging enabled.

**Rationale:**

S3 bucket logging provides visibility into the requests that are made to your buckets. This information can be used for security monitoring, troubleshooting, and access auditing.

**Remediation:**

Enable logging for your S3 buckets. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html).

## AWS-31-ebs-snapshot-public-restorable-check

**Rule Description:**

This rule checks whether your EBS snapshots are public.

**Rationale:**

EBS snapshots that are not intended to be shared with the public should not be made public. This prevents unauthorized users from creating volumes from your snapshots.

**Remediation:**

Do not make EBS snapshots public unless they are intended to be shared with the public. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html).

## AWS-32-encrypted-volumes

**Rule Description:**

This rule checks whether the EBS volumes that are attached to EC2 instances are encrypted.

**Rationale:**

Encrypting EBS volumes helps to protect the data that is stored on the volumes. This is a security best practice.

**Remediation:**

Enable encryption for your EBS volumes. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html).

## AWS-33-rds-storage-encrypted

**Rule Description:**

This rule checks whether storage encryption is enabled for your RDS DB instances.

**Rationale:**

Encrypting RDS DB instances helps to protect the data that is stored in the instances. This is a security best practice.

**Remediation:**

Enable storage encryption for your RDS DB instances. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html).

## AWS-34-rds-snapshots-public-prohibited

**Rule Description:**

This rule checks whether your RDS snapshots are public.

**Rationale:**

RDS snapshots that are not intended to be shared with the public should not be made public. This prevents unauthorized users from creating DB instances from your snapshots.

**Remediation:**

Do not make RDS snapshots public unless they are intended to be shared with the public. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html).

## AWS-35-rds-instance-public-access-check

**Rule Description:**

This rule checks whether your RDS DB instances are publicly accessible.

**Rationale:**

RDS DB instances that do not need to be accessed from the internet should not be publicly accessible. This reduces the attack surface of your AWS account.

**Remediation:**

Do not make your RDS DB instances publicly accessible. Instead, use a bastion host or a VPN to access the instances.

## AWS-36-rds-minor-version-upgrade-enabled

**Rule Description:**

This rule checks whether your RDS DB instances have minor version upgrades enabled.

**Rationale:**

Enabling minor version upgrades helps to ensure that your RDS DB instances are running the latest security patches and bug fixes.

**Remediation:**

Enable minor version upgrades for your RDS DB instances. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MinorVersionUpgrade.html).

## AWS-37-rds-logging-enabled

**Rule Description:**

This rule checks whether your RDS DB instances have logging enabled.

**Rationale:**

RDS logging provides visibility into the activity of your DB instances. This information can be used for security monitoring, troubleshooting, and performance analysis.

**Remediation:**

Enable logging for your RDS DB instances. For instructions on how to do this, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html).
