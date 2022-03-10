from multiprocessing import connection
import psycopg2

def getConnection():
    connection = psycopg2.connect(
    database="final_project",
    user="root", 
    password="password", 
    host="localhost", 
    port="5432"
    )

    return connection



