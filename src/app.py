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

cursor.execute('SELECT branch_id FROM branch')
for a in cursor:
    print(a[0])
    branch_id = a[0]

for item in processedData:
    data_row_insert_sql = f"""INSERT INTO transactions(date_time, branch_id)
    VALUES(to_timestamp('{item['date_time']}','DD/MM/YYYY HH24:MI'),{branch_id})"""    
    cursor.execute(data_row_insert_sql)
    connection.commit()



cursor.execute('SELECT branch_id FROM branch')
for a in cursor:
    print(a[0])
    branch_id = a[0]

for item in processedData:
    data_row_insert_sql = f"""INSERT INTO transactions(date_time, branch_id)
    VALUES(to_timestamp('{item['date_time']}','DD/MM/YYYY HH24:MI'),{branch_id})"""    
    cursor.execute(data_row_insert_sql)
    connection.commit()

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
            productName = productName.strip()
            productPrice = row[1] # get the price (second item)
            productPrice = productPrice.replace(" ","") #removing the space/s
            alteredProducts = {'product_name': productName,'product_price':productPrice} #creating a dict with new values
            finalProducts.append(alteredProducts) #appending Trans list to the global list
    
    return(finalProducts)

<<<<<<< HEAD
=======

<<<<<<< HEAD
#<-------- removing duplicates. (comment out if not needed atm!) -------->
=======
writingData = (cleaning(processedData))
>>>>>>> 99124bb96f0595a45c4f2ce45b6706d662efee68
writingData = (processedData)
# for item in writingData:
#     data_row_insert_sql = f"""INSERT INTO products(product_name, product_price)
#     VALUES('{item}['product_name']'), ('{item}['product_price']')"""    
#     cursor.execute(data_row_insert_sql)
#     connection.commit()
<<<<<<< HEAD
>>>>>>> accde067b195d06c4d58929ec266ae0d3a926a27

# removeDuplicates = (cleaning(processedData))

<<<<<<< HEAD
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
=======
def branch_location(processedData):
    branch_location_list = []
    branch_location_list_unique = []
    for item in processedData:
        branch_location = item['location']
        branch_location_list.append(branch_location)
        branch_location_list_unique = set(branch_location_list)
    return branch_location_list_unique


# writingData = (branch_location(processedData))
# for item in writingData:
#     data_row_insert_sql = f"""INSERT INTO branch(branch_location)
#     VALUES('{item}')"""    
#     cursor.execute(data_row_insert_sql)
#     connection.commit()
=======
>>>>>>> 99124bb96f0595a45c4f2ce45b6706d662efee68

def branch_location(processedData):
    branch_location_list = []
    branch_location_list_unique = []
    for item in processedData:
        branch_location = item['location']
        branch_location_list.append(branch_location)
        branch_location_list_unique = set(branch_location_list)
    return branch_location_list_unique

# writingData = (branch_location(processedData))
# for item in writingData:
#     data_row_insert_sql = f"""INSERT INTO branch(branch_location)
#     VALUES('{item}')"""    
#     cursor.execute(data_row_insert_sql)
#     connection.commit()


        
<<<<<<< HEAD

=======
>>>>>>> 99124bb96f0595a45c4f2ce45b6706d662efee68

cleaning(processedData) 

>>>>>>> accde067b195d06c4d58929ec266ae0d3a926a27
