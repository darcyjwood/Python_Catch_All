import boto3

client = boto3.client("s3")

client.create_bucket(Bucket="darcyboto3testbucket") 
