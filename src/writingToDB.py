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



insertIntoBranch(location)


    # currentBranchList = []
    # updatedBranchLocation = []
    # for item in processedData:
    #     branch_location = item['location']
    #     currentBranchList.append(branch_location)
    #     updatedBranchLocation = set(currentBranchList)
    # return updatedBranchLocation




# cursor.execute('SELECT branch_id FROM branch')
# for a in cursor:
#     print(a[0])
#     branch_id = a[0]

# for item in processedData:
#     data_row_insert_sql = f"""INSERT INTO transactions(date_time, branch_id)
#     VALUES(to_timestamp('{item['date_time']}','DD/MM/YYYY HH24:MI'),{branch_id})"""    
#     cursor.execute(data_row_insert_sql)
#     connection.commit()



# cursor.execute('SELECT branch_id FROM branch')
# for a in cursor:
#     print(a[0])
#     branch_id = a[0]

# for item in processedData:
#     data_row_insert_sql = f"""INSERT INTO transactions(date_time, branch_id)
#     VALUES(to_timestamp('{item['date_time']}','DD/MM/YYYY HH24:MI'),{branch_id})"""    
#     cursor.execute(data_row_insert_sql)
#     connection.commit()


#<-------- removing duplicates. (comment out if not needed atm!) -------->
# writingData = (cleaning(processedData))
# writingData = (processedData)
# for item in writingData:
#     data_row_insert_sql = f"""INSERT INTO products(product_name, product_price)
#     VALUES('{item}['product_name']'), ('{item}['product_price']')"""    
#     cursor.execute(data_row_insert_sql)
#     connection.commit()






# writingData = (branch_location(processedData))
# for item in writingData:
#     data_row_insert_sql = f"""INSERT INTO branch(branch_location)
#     VALUES('{item}')"""    
#     cursor.execute(data_row_insert_sql)
#     connection.commit()
