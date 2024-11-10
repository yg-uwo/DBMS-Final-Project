import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='.env.yash')
 

def create_connection():
    connection = mysql.connector.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USERNAME'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DBNAME')
    )
    return connection.cursor()