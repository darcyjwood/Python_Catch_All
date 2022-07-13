import boto3

ec2_resource = boto3.resource("ec2")

x = ec2_client.describe_instances()

data = x["Reservations"]

li - []
for instances in data:
    instance = instances["Instances"]
    for ids in instances:
        instance_id = ids["InstanceId"]
        li.append(instance_id)

ec2_client.terminate_instances(InstanceIds = li)


    
