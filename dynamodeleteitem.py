import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('WoodCafe')

response = table.delete_item(
    Key = {
        'Special': 'cubano',
        'Price': int('9')
    }
)

print(response)