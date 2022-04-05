def createTables():
    connection = getConnection()
    cursor = connection.cursor()
    branch_table = '''CREATE TABLE IF NOT EXISTS mercury.branch(
    branch_id INT IDENTITY(1,1) PRIMARY KEY,
    branch_location VARCHAR(100) NOT NULL
    );
    '''
    
    product_table = '''CREATE TABLE IF NOT EXISTS mercury.product(
    product_id INT IDENTITY(1,1) PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    product_price FLOAT
    );
    '''
    
    transaction_table = '''CREATE TABLE IF NOT EXISTS mercury.transaction(
    transaction_id INT IDENTITY(1,1) PRIMARY KEY,
    date_time TIMESTAMP,
    branch_id INT,
    CONSTRAINT fk_branch FOREIGN KEY(branch_id) REFERENCES mercury.branch(branch_id)
    );
    '''
    
    basket_table = '''CREATE TABLE IF NOT EXISTS mercury.basket(
    product_id INT,
    transaction_id INT,
    CONSTRAINT fk_product_id FOREIGN KEY(product_id) REFERENCES mercury.product(product_id),
    CONSTRAINT fk_transaction FOREIGN KEY(transaction_id) REFERENCES mercury.transaction(transaction_id)
    );
    '''
    
    cursor.execute(branch_table)
    cursor.execute(product_table)
    cursor.execute(transaction_table)
    cursor.execute(basket_table)
    connection.commit()
    cursor.close()
    connection.close()    
