#creates a basic SQS Queue

import boto3 
import time

#get the service resource
sqs = boto3.resource('sqs')

#get the queue and give name and attributes
queue = sqs.create_queue(QueueName = 'MySQSQueue', Attributes = {'DelaySeconds': '5'})

print(queue.url)
print(queue.attributes.get('DelaySeconds'))