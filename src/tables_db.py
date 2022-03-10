import db

#<-------- Create Connection from DB.py -------->
connection = db.getConnection()
cursor = connection.cursor()


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

chesterfield_table = """
CREATE TABLE IF NOT EXISTS chesterfield(
date_Time Date,
location VARCHAR(100),
full_name VARCHAR(100),
orders VARCHAR(100),
amount int NOT NULL,
payment_type VARCHAR(100)
);
"""

cursor.execute(product_table)
cursor.execute(transaction_table)
cursor.execute(branch_table)
cursor.execute(basket_table)
cursor.execute(chesterfield_table)
connection.commit()