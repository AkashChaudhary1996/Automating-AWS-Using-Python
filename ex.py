# coding: utf-8
import boto3
session=boto3.Session()
s3=session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
new_bucket=s3.create_bucket(Bucket='cakashku')
for bucket in s3.buckets.all():
    print(bucket)
    
ec2_client=session.client('ec2')
ec2_client
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'history.py')
