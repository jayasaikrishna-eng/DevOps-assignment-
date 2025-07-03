import boto3
import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = "your-unique-bucket-name"  # Replace with actual bucket name
    key = f"lambda-run-{datetime.datetime.now().isoformat()}.txt"
    content = "Lambda function ran at " + datetime.datetime.now().isoformat()
    s3.put_object(Bucket=bucket, Key=key, Body=content.encode())
    return {"message": "Object uploaded to S3", "key": key}
