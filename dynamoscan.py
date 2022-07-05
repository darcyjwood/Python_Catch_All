import boto3
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('WoodCafe')

response = table.scan()

data = response['Items']

while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    data.extend(response['Items'])

print(data)