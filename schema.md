# Scheme design to model data

**These are sample database tables we want transfer our data into. We have chosen our fieldnames which are in the tables**

**The way the tables have been designed could:**
1. Help answer queries and make it straightforward as possible
2. Solve problems within the data
3. Remove and transform data
4. Help identify trends and insights

## Table : Basket
| -----------| -----------    | 
|  order_ID  |   product_Id   | 
|     INT    |      INT       |       
|            |                |             

## Table : Products
| -----------| -----------   | ------------- |
| product_ID | product_name  | product_price |
|     INT    |     VAR       |    FLOAT      | 
|            |               |               |            

## Table : Transaction
| -----------| -----------    | ---------------| 
|  order_ID  |  product_price |   order_total  |
|    INT     |     FLOAT      |     NUMERIC    |   
|            |                |                |

