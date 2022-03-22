from concurrent.futures import process
from itertools import product
from optparse import Values
import re
from tkinter import S
import db
from cleaningData import *

############################################################################
#                                                                          #
#                   Writing to the database tables only!                   #
#                                                                          #
############################################################################

#<-------- Create Connection from DB.py -------->

connection = db.getConnection()
cursor = connection.cursor()

###################################################################################


#<-------- Insert into DB functions -------->

# We're getting the data from the extract function and from the database
# We're then cross refrencing/checking the DB if it has the location.
# If the location is in the DB then we do nothing.
# If it doesn't exist then we append the location to the newBranch list.
# Finally we commit to the DB.



def insertIntoBranch(location):
    
    with cursor:
        cursor.execute('SELECT branch_id FROM branch WHERE branch_location = %s', location)
        branch_id = cursor.fetchone()

        if not branch_id:
            sql = f"""INSERT INTO branch("branch_location")VALUES('{location}')"""  
            cursor.execute(sql)
            cursor.execute('SELECT branch_id FROM branch WHERE branch_location = %s', location)
            branch_id = cursor.fetchone()
        connection.commit()
        return branch_id[0]

###################################################################################

# Getting the data from Extract function
# Getting the ID's from the branch table in DB if there are any
# Getting the timestamp via indexing and writing the branch id to the respective time



def insertIntoTransaction(branch_id, transaction_data):
    with cursor:

        sql = f"""INSERT INTO transaction(date_time, branch_id)
        VALUES (to_timestamp('{transaction_data['date_time']}','DD/MM/YYYY HH24:MI'),{branch_id})
        """    
        cursor.execute(sql)
        connection.commit()

###################################################################################



def insertIntoProducts(product):
    product_name = product['product_name']
    product_price = product['product_price']
    with cursor:
        cursor.execute('SELECT product_id FROM product WHERE product_name = %s AND product_price = %s', (product_name, product_price))
        products_id = cursor.fetchone()
        
        if not products_id:
            sql = f"""INSERT INTO product(product_name, product_price)
            VALUES ('{product_name}','{product_price}')"""
            cursor.execute(sql)
            cursor.execute('SELECT product_id FROM product WHERE product_name = %s AND product_price = %s', (product_name, product_price))
            products_id = cursor.fetchone()
            connection.commit()
        return products_id[0]



def insert_into_basket_table(product_id, transaction_id):
    with cursor:

        sql_basket = f"""INSERT INTO basket(product_id, transaction_id)
        VALUES ('{product_id}', '{transaction_id}')"""   
        cursor.execute(sql_basket)
        connection.commit()
        
processedData = ExtractData(file)
#data = splittingData(processedData)
#location = branchLocation(location)

for row in processedData:
    branch_id = insertIntoBranch(row['branch'])
    transaction_id = insertIntoTransaction(branch_id, row)
    basket = row['orders']
    individualorders = basket.split(",")
    for order in individualorders:
        order = order.rsplit("-",1)
        productName = order[0]
        productName = productName.strip()
        productPrice = order[1]
        productPrice = productPrice.replace(" ","")
        alteredProducts = {'product_name': productName,'product_price':productPrice}
        product_id = insertIntoProducts(alteredProducts)
        insert_into_basket_table(product_id, transaction_id)
        

#insertIntoProducts(data)
#print(splittingData(data))
#insertIntoBranch(location)
#insertIntoTransaction(data)
#insertIntoProducts(data)
