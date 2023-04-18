import boto3
import json

iam = boto3.client('iam')

role_name = 'my-iam-role-name'

assume_role_policy_document = json.dumps({
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": {
            "Service": "lambda.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
    }]
})

response = iam.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument=assume_role_policy_document,
    Path='/'
)

policy_arn = 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
response = iam.attach_role_policy(
    RoleName=role_name,
    PolicyArn=policy_arn
)

print(response)
