import boto3

client = boto3.client("ec2")

response = client.delete_vpc(
    VpcId = 'vpc-00d828f88c7256463')
    
    