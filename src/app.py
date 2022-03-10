import csv
from itertools import product
from optparse import Values
import db

#<-------- Create Connection from DB.py -------->

connection = db.getConnection()
cursor = connection.cursor()


#<-------- Extract Data -------->

file = '../chesterfield1.csv'

def ExtractData(file):
    with open(file, 'r') as file:

        fullDataFromCSV = []

        fieldnames=['date_time','location','Full_Name','orders','amount','payment_type','Card_Details']
        dict_reader = csv.DictReader(file, fieldnames = fieldnames, delimiter=',')

        for item in dict_reader:
            item = dict(item)        
            if 'Card_Details' in item: del item['Card_Details']
            if 'Full_Name' in item: del item['Full_Name']
            else: break
            fullDataFromCSV.append(item)

        return(fullDataFromCSV)


fullDataFromCSV = ExtractData(file)

for data_row in fullDataFromCSV:
    data_row_insert_sql = f"""INSERT INTO chesterfield(date_time, location, orders, amount, payment_type)
    VALUES('{data_row['date_time']}', 
            '{data_row['location']}', 
            '{data_row['orders']}',
            '{data_row['amount']}', 
            '{data_row['payment_type']}')""" 
    values = "%s, %s, %s, %s, %s"
    cursor.execute(data_row_insert_sql, values)
    connection.commit()
         


# for data_row in fullDataFromCSV:
#             data_row_insert_sql = f"""INSERT INTO chesterfield(date_time, Location, orders, amount, payment_type)
#             VALUES('{data_row['date_time']}', '{data_row['Location']}', '{data_row['orders']}',
#             {data_row['amount']}, '{data_row['payment_type']}')"""    
#             cursor.execute(data_row_insert_sql)

#             connection.commit()
        
#             return(fullDataFromCSV)



#<-------- Create DB Fields -------->

basket_table = """
CREATE TABLE IF NOT EXISTS basket(
product_id int NOT NULL,
transaction_id int NOT NULL
);
"""
branch_table = """
CREATE TABLE IF NOT EXISTS branch(
cafe_id int NOT NULL,
location VARCHAR(100)
);
"""
product_table = """
CREATE TABLE IF NOT EXISTS products(
product_id int NOT NULL,
product_name VARCHAR(100),
product_size VARCHAR(100),
product_price FLOAT
);
"""
transaction_table = """
CREATE TABLE IF NOT EXISTS transactions (
date_time DATE,
transaction_id int NOT NULL,
cafe_id int NOT NULL
);
"""

cursor.execute(product_table)
cursor.execute(transaction_table)
cursor.execute(branch_table)
cursor.execute(basket_table)
connection.commit()


ExtractData(file)
        

