import boto3
import os
import glob

s3_resource = boto3.client("s3")

#s3_resource.delete_object(Bucket = "darcyboto3testbucket", 
    #Key = "upload2.png")
    
cwd = os.getcwd()

objects = s3_resource.list_objects(Bucket = "darcyboto3testbucket")["Contents"]

len(objects)

for object in objects:
    s3_resource.delete_object(Bucket = "darcyboto3testbucket", 
    Key = object["Key"])
    print(object["Key"])