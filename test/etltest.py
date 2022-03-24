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

################################## < creating a test tabel in Lambda > #############################################

connection = getConnection()
    cursor = connection.cursor()

    result = cursor.execute("""
        CREATE TABLE IF NOT EXISTS mercury.roshnis_test_table(
        branch_id INT IDENTITY(1,1) PRIMARY KEY,
        branch_location VARCHAR(100) NOT NULL)
    """)
    
    data = cursor.execute("""
        INSERT INTO mercury.roshnis_test_table(product_id, product_location) VALUES (100, 'leeds')
    """)
    connection.commit()
    cursor.close()
    connection.close()
    
    result = ("""
        select * from mercury.roshnis_test_table
    """)
    
    items = cursor.execute(result)
    items = cursor.fetchall()
    for item in items: