import db

#<-------- Create Connection from DB.py -------->
connection = db.getConnection()
cursor = connection.cursor()


basket_table = """
CREATE TABLE IF NOT EXISTS basket(
order_id SERIAL,
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
order_id int NOT NULL,
order_total numeric
);
"""

chesterfield_table = """
CREATE TABLE IF NOT EXISTS chesterfield(
date_Time Date,
location VARCHAR(100),
full_name VARCHAR(100),
orders VARCHAR(500),
amount numeric,
payment_type VARCHAR(100)
);
"""

cursor.execute(product_table)
cursor.execute(transaction_table)
cursor.execute(basket_table)
cursor.execute(chesterfield_table)
connection.commit()