import os
import time
import boto3

# Function to list files in a directory
def list_files(directory):
    return os.listdir(directory)

# Function to upload a file to S3
def upload_to_s3(file_path, bucket_name, s3_folder):
    s3 = boto3.client('s3')
    file_name = os.path.basename(file_path)
    s3_key = os.path.join(s3_folder, file_name)
    s3.upload_file(file_path, bucket_name, s3_key)

# Directory to monitor
directory = '/home/admin/dockerimg'

# S3 bucket details
bucket_name = 'cutiedelaborator'
s3_folder = 'dockers/'

# Set AWS credentials file path
os.environ['AWS_SHARED_CREDENTIALS_FILE'] = '/path/to/aws/credentials/file'

# Main loop to monitor the directory
while True:
    files = list_files(directory)
    for file in files:
        file_path = os.path.join(directory, file)
        upload_to_s3(file_path, bucket_name, s3_folder)
        print(f"Uploaded {file} to S3")
    time.sleep(10)  # Check every 60 seconds
