import db

#<-------- Create Connection from DB.py -------->
connection = db.getConnection()
cursor = connection.cursor()

branch_table = '''CREATE TABLE IF NOT EXISTS branch(
branch_id SERIAL PRIMARY KEY,
branch_location VARCHAR(100) NOT NULL
);
'''

product_table = '''CREATE TABLE IF NOT EXISTS product(
product_id SERIAL PRIMARY KEY,
product_name VARCHAR(100) NOT NULL,
product_price FLOAT
);
'''

transaction_table = '''CREATE TABLE IF NOT EXISTS transaction(
transaction_id SERIAL PRIMARY KEY,
date_time TIMESTAMP,
branch_id INT,
CONSTRAINT fk_branch FOREIGN KEY(branch_id) REFERENCES branch(branch_id)
);
'''

basket_table = '''CREATE TABLE IF NOT EXISTS basket(
product_id INT,
transaction_id INT,
CONSTRAINT fk_product_id FOREIGN KEY(product_id) REFERENCES product(product_id),
CONSTRAINT fk_transaction FOREIGN KEY(transaction_id) REFERENCES transaction(transaction_id)
);
'''


cursor.execute(branch_table)
cursor.execute(product_table)
cursor.execute(transaction_table)
cursor.execute(basket_table)
connection.commit()



############## DROP ALL TABLES (COMMENT OUT IF NOT NEEDED) ##########################

# sql = "DROP TABLE basket, branch, product, transaction"
# cursor.execute(sql)
# connection.commit()

#####################################################################################