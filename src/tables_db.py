import db

############################################################################
#                                                                          #
#      This file is responsible for creating the database tables only!     #
#                                                                          #
############################################################################


#<-------- Create Connection from DB.py -------->
connection = db.getConnection()
cursor = connection.cursor()


basket_table = """
CREATE TABLE IF NOT EXISTS basket(
transaction_id SERIAL,
product_id SERIAL   
);
"""

product_table = """
CREATE TABLE IF NOT EXISTS products(
product_id int NOT NULL,
product_name VARCHAR(100),

product_price FLOAT
);
"""
transaction_table = """
CREATE TABLE IF NOT EXISTS transactions(
transaction_id SERIAL,
date_time TIMESTAMP,
branch_id int NOT NULL
);
"""
branch_table = """
CREATE TABLE IF NOT EXISTS branch(
branch_id SERIAL,
branch_location VARCHAR(100)
);
"""



cursor.execute(product_table)
cursor.execute(transaction_table)
cursor.execute(basket_table)
cursor.execute(branch_table)
connection.commit()