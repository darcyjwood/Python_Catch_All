import json
import boto3

from datetime import datetime

def lambda_handler(event, context):
    
    now = datetime.now()
    date_time = now.strftime('%m/%d/%Y, %H:%M:%S:%p')
    
    sqs = boto3.client("sqs")
    sqs.send_message(
        QueueUrl = 'https://sqs.us-east-1.amazonaws.com/xxxxxxxxxxxx/MySQSQueue',
        MessageBody = date_time
        )

    return {
        'statusCode': 200,
        'body': json.dumps(date_time)
    }
    