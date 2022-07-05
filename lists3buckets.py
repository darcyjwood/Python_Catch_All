import boto3

s3 = boto3.client('s3')

list buckets
response = s3.list_buckets()

buckets = response["Buckets"]

for bucket in buckets:
    print(bucket["Name"])