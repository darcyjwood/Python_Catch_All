import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('WoodCafe')

response = table.put_item(
    Item = {
        'Special': 'cubano',
        'Price': int('9')
    }
)
print(response)
