import boto3
import json
import os

# AWS Rekognition Client
rekognition = boto3.client('rekognition')

def tag_image(bucket, image):
    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': image
            }
        },
        MaxLabels=10,
        MinimumConfidence=75
    )
    return response['Labels']

if __name__ == '__main__':
    bucket_name = 'your-bucket-name'
    image_name = 'example.jpg'
    labels = tag_image(bucket_name, image_name)
    print(json.dumps(labels, indent=4))
