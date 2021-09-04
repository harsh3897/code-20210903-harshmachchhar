import boto3
import json
import os

s3 = boto3.client('s3')

s3_bucket_name = os.environ['s3_bucket_name']
print(s3_bucket_name)

def lambda_handler(event, context):
    #Get Message from SQS Event
    
    body = event['Records'][0]['body']
    message_load = json.loads(body)
    type = message_load['Type']
    message_id = message_load['MessageId']
    subject = message_load['Subject']
    message = message_load['Message']
    
    #Put Message body to S3 Bucket
    
    put = s3.put_object(Body=json.dumps(message_load), Bucket=f"{s3_bucket_name}", Key='body.json')
    
    
