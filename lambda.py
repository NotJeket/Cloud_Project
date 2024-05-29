import json
import boto3

def lambda_handler(event, context):
    sns_topic_arn = '*******************************'
    sns_message = 'A new job was done in the /dockers folder of the S3 bucket.'

    # Extract information from the S3 event
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        # Check if the object key belongs to the /dockers folder
        if object_key.startswith('dockers/'):
            # Process the object key as needed
            # Publish message to SNS topic
            sns_client = boto3.client('sns')
            sns_client.publish(TopicArn=sns_topic_arn, Message=sns_message)

    return {
        'statusCode': 200,
        'body': json.dumps('SNS notification sent successfully!')
    }

