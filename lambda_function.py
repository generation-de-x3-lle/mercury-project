import psycopg2
import boto3 
import os
import csv
import urllib
import new_table
import db
import cleaningData
import writingToDB

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    s3_object = s3.get_object(Bucket=bucket, Key=key)
    data = s3_object['Body'].read().decode('utf-8')

    file = data.splitlines()
    
    new_table.createTables()
    connection = db.getConnection()
    cursor = connection.cursor()
    
    processedData = cleaningData.ExtractData(file)
    writingToDB(processedData)

    