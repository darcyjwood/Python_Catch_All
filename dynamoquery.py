import boto3

from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('WoodCafe')

print("How much are greens?")

response = table.query(
    KeyConditionExpression=Key('Special').eq('greens')
)

for i in response['Items']:
        print(i['Special'], ":", i['Price'])