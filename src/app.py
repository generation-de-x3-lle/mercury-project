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



def cleaning(processedData):
    finalProducts = [] #global list which will contain all transactions

    for singleItem in processedData:
        allOrders = (singleItem['orders']) #only getting the orders from the file
        individualorder = allOrders.split(",") #splitting each instance
    
        for row in individualorder:
            row = row.rsplit("-",1) #splitting via the dash only once
            productName = row[0]  # get the name(first item)
            productPrice = row[1] # get the price (second item)
            productPrice = productPrice.replace(" ","") #removing the space/s
            alteredProducts = {'product_name': productName,'product_price':productPrice} #creating a dict with new values
        
            finalProducts.append(alteredProducts) #appending Trans list to the global list

    return(finalProducts)


writingData = (cleaning(processedData))
writingData = (processedData)
# for item in writingData:
#     data_row_insert_sql = f"""INSERT INTO products(product_name, product_price)
#     VALUES('{item}['product_name']'), ('{item}['product_price']')"""    
#     cursor.execute(data_row_insert_sql)
#     connection.commit()

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

for item in writingData:
    data_row_insert_sql = f"""INSERT INTO chesterfield(product_name, product_price)
    VALUES('{item['product_name']}', '{item['product_price']}')"""    
    cursor.execute(data_row_insert_sql)

    connection.commit()
        

cleaning(processedData) 

