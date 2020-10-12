# -*- coding: utf-8 -*-
""" Information from: https://realpython.com/python-boto3-aws-s3/#:~:text=Boto3%20is%20the%20name%20of,resources%20from%20your%20Python%20scripts. 
"""

import boto3
import uuid

"""s3 client creation"""
s3_client = boto3.client('s3')

"""s3 resource creation"""
s3_resource = boto3.resource('s3')

"""Generates bucket name"""
def create_bucket_name (bucket_prefix):
        return ''.join([bucket_prefix, str(uuid.uuid4())])
    
"""Generates bucket"""
def create_bucket (bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={ 'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response


"""Generates file name"""
def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    return random_file_name



first_bucket_name, first_response = create_bucket(bucket_prefix='firstpythonbucket', s3_connection=s3_resource.meta.client)
second_bucket_name, second_response = create_bucket(bucket_prefix='secondpythonbucket', s3_connection=s3_resource)

first_file_name = create_temp_file(300, 'firstfile.txt', 'f')

first_bucket = s3_resource.Bucket(name=first_bucket_name)
first_object = s3_resource.Object(bucket_name=first_bucket_name, key=first_file_name)

s3_resource.meta.client.upload_file(Filename=first_file_name, Bucket=first_bucket_name, Key=first_file_name)