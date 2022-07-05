import boto3
import os
import glob

#to upload a single file
s3_resource = boto3.client("s3")

#s3_resource.upload_file(
    #Filename = "bio.py",
    #Bucket = "darcyboto3testbucket", 
    #Key = "biotest.py",)

#cwd = "Python_Catch_All"

cwd = os.getcwd()

#cwd = cwd + "/upload"

files = glob.glob(cwd + "/*.py")

for file in files:
    s3_resource = boto3.client("s3")
    s3_resource.upload_file(
        Filename = file,
        Bucket = "darcyboto3testbucket",
        Key = file.split("/")[-1])
        
print(cwd)
print(files)