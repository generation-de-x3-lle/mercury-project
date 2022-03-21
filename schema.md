# Scheme design to model data

**These are sample database tables we want transfer our data into. We have chosen our fieldnames which are in the tables**

**The way the tables have been designed could:**
1. Help answer queries and make it straightforward as possible
2. Solve problems within the data
3. Remove and transform data
4. Help identify trends and insights

## Table : Basket
| -----------------| ---------------| 
|  transaction_ID  |   product_ID   | 
|       INT        |      INT       |       
|                  |                |             

## Table : Products
| -----------| -----------   | ------------- |
| product_ID | product_name  | product_price |
|     INT    |   VARCHAR     |    FLOAT      | 
|            |               |               |         

## Table : Branch
| -----------| -----------------|
| branch_ID  | branch_location  | 
|    INT     |     VARCHAR      |    
|            |                  |                 

## Table : Transaction
| ---------------- | ------------| -----------------------|
|  transaction_ID  |  date_time  |       branch_ID        |
|        INT       |   VARCHAR   |  INT(FK to branch_ID)  |
|                  |             |                        |