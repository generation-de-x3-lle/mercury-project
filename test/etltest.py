import psycopg2
import boto3 
import os
import csv



s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = 'de-x3-lle-mercury'
    key = '2022/3/16/chesterfield_16-03-2022_09-00-00.csv'
    filename = s3.get_object(Bucket=bucket, Key =key)
    
    lines = filename['Body'].read().decode('utf-8').splitlines(True)
    reader = csv.reader(lines)
    
    for line in reader:
        print(line)