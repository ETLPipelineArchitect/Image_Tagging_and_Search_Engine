import boto3
import os

# AWS S3 Client
s3 = boto3.client('s3')

def download_images(bucket_name, prefix):
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    for obj in response['Contents']:
        file_name = obj['Key'].split('/')[-1]
        s3.download_file(bucket_name, obj['Key'], file_name)

if __name__ == '__main__':
    bucket = 'your-bucket-name'
    prefix = 'images/'
    download_images(bucket, prefix)
