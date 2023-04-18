import boto3

s3 = boto3.client('s3')

bucket_name = 'my-s3-bucket-name'

response = s3.create_bucket(
    Bucket=bucket_name,
)

print(response)
