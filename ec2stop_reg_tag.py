import json
import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

#def lambda_handler(event, context):
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['Running']},{'Name': 'tag:Enironment','Values':['Dev']}])#enter your EC2 tag key and id where I have "test1" and "test1pair"
for instance in instances:
    id=instance.id
    ec2.instances.filter(InstanceIds=[id]).stop()
    print("Instance ID is started :- "+instance.id)
        #return "success"