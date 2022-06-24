#project using aws service list

services = []

#['s3', 'cloudfront', 'beanstalk', 'lambda', 'dynamodb', 'sqs', 'ec2']

services.append('s3')

print(services)

services.append('cloudfront')
services.append('beanstalk')
services.append('lambda')
services.append('dynamodb')
services.append('sqs')
services.append('ec2')

print(services)

print(len(services))

del services [2]

print(services)

del services [1]

print(services)

print(len(services))







