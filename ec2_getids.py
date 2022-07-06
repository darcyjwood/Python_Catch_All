import boto3

ec2_client = boto3.client("ec2")
x = ec2_client.describe_instances()

data = x["Reservations"][0]
data_instance = data["Instances"]

for i in range(len(data_instance)):
    print(f"instance id is {data_instance[i]['InstanceId']}")
    
