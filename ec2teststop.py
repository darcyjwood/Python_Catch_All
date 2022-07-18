import boto3
region = 'us-east-1'

ec2 = boto3.client('ec2', region_name='region')

instances = ec2.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['Running']},{'Name': 'Environment','Values':['Dev']}])

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))