from concurrent.futures import process
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

processedData = (ExtractData(file))


#<-------- cleaning the raw data-------->

def cleaning(processedData):
    finalProducts = [] #global list which will contain all transactions

    for singleItem in processedData:
        #row
        allOrders = (singleItem['orders']) #only getting the orders from the file
        individualorder = allOrders.split(",") #splitting each instance
    
        #indivdual item
        for row in individualorder:
            row = row.rsplit("-",1) #splitting via the dash only once
            productName = row[0]  # get the name(first item)
            productPrice = row[1] # get the price (second item)
            productPrice = productPrice.replace(" ","") #removing the space/s
            alteredProducts = {'product_name': productName,'product_price':productPrice} #creating a dict with new values
            finalProducts.append(alteredProducts) #appending Trans list to the global list
    
    return(finalProducts)


#<-------- removing duplicates. (comment out if not needed atm!) -------->

# removeDuplicates = (cleaning(processedData))

# def remove_duplicate(removeDuplicates):
#     newList = []
#     for item in removeDuplicates:
#         if item not in newList:
#             newList.append(item)
#     return newList


# #<-------- Create DB Fields -------->

# basket_table = """
# CREATE TABLE IF NOT EXISTS basket(
# product_id int NOT NULL,
# transaction_id int NOT NULL
# );
# """
# branch_table = """
# CREATE TABLE IF NOT EXISTS branch(
# cafe_id int NOT NULL,
# location VARCHAR(100)
# );
# """
# product_table = """
# CREATE TABLE IF NOT EXISTS products(
# product_id int NOT NULL,
# product_name VARCHAR(100),
# product_size VARCHAR(100),
# product_price FLOAT
# );
# """
# transaction_table = """
# CREATE TABLE IF NOT EXISTS transactions (
# date_time DATE,
# transaction_id int NOT NULL,
# cafe_id int NOT NULL
# );
# """

# cursor.execute(product_table)
# cursor.execute(transaction_table)
# cursor.execute(branch_table)
# cursor.execute(basket_table)
# connection.commit()


#ExtractData(file)
#cleaning(processedData) 
print(remove_duplicate(removeDuplicates))
