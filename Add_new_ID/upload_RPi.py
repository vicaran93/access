

import boto
import sys
import os
import botocore
import boto3

'''
    This program uploads a file with public permissions to an aws S3 bucket.
    Three environment variables must be setup accordingly:  AWS_ACCESS_KEY_ID  AWS_SECRET_ACCESS_KEY BUCKET

'''
# Check correct amount of inputs:
path="/home/pi/Documents/access/camera/"#"C:/Users/Victor/Documents/UMass Amherst/Fall 2017 (senior)/SDP/images/"  # path without image name
# Check input name
if len(sys.argv) != 2:
    print("No input name detected!")
    sys.exit("No input detected! Name of the file without extension must be provided as input through console")

file_name = sys.argv[1]
file_path = path+file_name+".jpg" # assuming jpg extension which is the one that we use when we take a picture


# Get Environment variables
aws_access_key = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_key = os.environ['AWS_SECRET_ACCESS_KEY']
aws_s3_bucket_name = os.environ['BUCKET']
print(aws_s3_bucket_name) # check
# Authenticate connection
conn = boto.connect_s3(aws_access_key, aws_secret_key)
# Get Bucket
s3 = boto3.resource('s3')
aws_s3_bucket = s3.Bucket(aws_s3_bucket_name)
exists = True
try:
    s3.meta.client.head_bucket(Bucket=aws_s3_bucket_name)
except botocore.exceptions.ClientError as e:
    # If a client error is thrown, then check that it was a 404 error.
    # If it was a 404 error, then the bucket does not exist.
    error_code = int(e.response['Error']['Code'])
    if error_code == 404:
        exists = False

# Bucket is opened. Now we can uload file to Bucket
#file_path ='2018-01-27_1251_cropped_bw.jpg'
image_name = 'T2.jpg'
# data = open('2018-01-27_1251_cropped_bw.jpg', 'rb')
# Upload image:
s3 = boto3.client('s3')
with open(file_path, 'rb') as data:
    s3.upload_file(
        file_path, aws_s3_bucket_name, image_name,
        ExtraArgs={'ACL': 'public-read'}
    )





