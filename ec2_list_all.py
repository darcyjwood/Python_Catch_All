import boto3

ec2 = boto3.resource('ec2')

ec2_client = boto3.client("ec2")


instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    
for instance in instances:
    print(instance.id, instance.instance_type)