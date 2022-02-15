from helper_functions import remove_start_end_spaces, fuzzyMatcher, clean_phase1, clean_phase2
import boto3
import openpyxl
import fsspec
import s3fs
import pandas as pd
import numpy as np
import uuid

s3_client = boto3.client("s3")
S3_BUCKET_NAME = 'BUCKET_NAME_HERE'
S3_BUCKET_PREFIX = 'PREFIX_HERE'

"""Get S3 object with AWS Lambda"""

def lambda_handler(event, context):   
    response = s3_client.list_objects_v2(Bucket=S3_BUCKET, Prefix=S3_PREFIX)
    s3_files = response["Contents"]
    for s3_file in s3_files:
        file_content = s3_client.get_object(Bucket=S3_BUCKET,Key=s3_file["Key"])["Body"].read()
        print(file_content)