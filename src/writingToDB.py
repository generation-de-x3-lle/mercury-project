from concurrent.futures import process
from itertools import product
from optparse import Values
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

def insertIntoBranch():
    #take in name of the branch
    # get branch id
    # if different brnach 
    
    
    
    currentBranchList = []
    updatedBranchLocation = []
    for item in processedData:
        branch_location = item['location']
        currentBranchList.append(branch_location)
        updatedBranchLocation = set(currentBranchList)
    return updatedBranchLocation




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
