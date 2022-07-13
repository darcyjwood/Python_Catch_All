#create 3 ec2s

import boto3

ec2_resource = boto3.resource("ec2")
#this will generate instances based on type and ammount and will tag them
result = ec2_resource.create_instances(ImageId = 'ami-0cff7528ff583bf9a',
      InstanceType = 't2.micro',
      MaxCount = 3,
      MinCount = 3,
      TagSpecifications = [
                           {
                               'ResourceType': 'instance',
                               'Tags': [{'Key': 'Environment','Value': 'Dev'}],
                           },
                       ],
                       )

print(result)
