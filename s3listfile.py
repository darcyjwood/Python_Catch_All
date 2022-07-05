import boto3

s3_resource = boto3.client("s3")

objects = s3_resource.list_objects(Bucket = "darcyboto3testbucket")["Contents"]

print(len(objects))

for object in objects:
    print(object["Key"])