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

location = branchLocation(location)

def insertIntoBranch(location):
    branchLocation = location
    newBranch = []
    
    
    with cursor:
        cursor.execute('SELECT * FROM branch')
        branchInDB = cursor.fetchall()

        for branch in branchLocation: 
            doesItAlreadyExist = False
            
            for value in branchInDB:
                if branch == value[1]:
                    doesItAlreadyExist = True
                    break
            if doesItAlreadyExist == False:
                newBranch.append(branch)

        for item in newBranch:
            sql = f"""INSERT INTO branch("branch_location")VALUES('{item}')"""  
            cursor.execute(sql)
        connection.commit()


###################################################################################

# Getting the data from Extract function
# Getting the ID's from the branch table in DB if there are any
# Getting the timestamp via indexing and writing the branch id to the respective time


data = ExtractData(file)

def insertIntoTransaction(data):
    with cursor:
        cursor.execute('SELECT branch_id FROM branch')

        for id in cursor:
            branch_id = id[0] #<------------Getting the ID only
            #print(branch_id) #<------------ prints "1" (Chesterfield) since there is only one in db

        for item in processedData:
            sql = f"""INSERT INTO transaction(date_time, branch_id)
            VALUES (to_timestamp('{item['date_time']}','DD/MM/YYYY HH24:MI'),{branch_id})
            """    
            cursor.execute(sql)
        connection.commit()


###################################################################################

data = splittingData(processedData)

def insertIntoProducts(data):
    
    notDuplicatedProducts= []

    with cursor:
        cursor.execute('SELECT * FROM product')
        productsInDB = cursor.fetchall()
        #print(productsInDB) #<---- [(70, 'Regular Flavoured iced latte - Hazelnut', 2.75), (71, 'Large Latte', 2.45), (72, 'Large Latte', 2.45)]
            
        for product in data: #<-------------------- products in the list
            doesItAlreadyExist = False    
            for value in productsInDB: #<-------------------- products in the database#

                if product["product_name"] == value[1] and str(product["product_price"]) == str(value[2]): #make sure they're in the same format
                    doesItAlreadyExist = True
                    break
            if doesItAlreadyExist == False:
                notDuplicatedProducts.append(product)
        
        for item in notDuplicatedProducts:
            sql = f"""INSERT INTO product(product_name, product_price)
            VALUES ('{item['product_name']}','{item['product_price']}')"""
            cursor.execute(sql)
            connection.commit()

#insertIntoProducts(data)
#print(splittingData(data))

#insertIntoBranch(location)
#insertIntoTransaction(data)
insertIntoProducts(data)
