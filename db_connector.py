import mysql.connector
from dotenv import load_dotenv
# load_dotenv(dotenv_path='/.env.jot')
import os

load_dotenv()

# Function to create a connection to MySQL database
def create_connection():
    connection = mysql.connector.connect(
        host=os.getenv('HOST'),  
        user=os.getenv('USERNAME'),     
        password=os.getenv('PASSWORD'), 
        database=os.getenv('DBNAME') 
    )
    return connection

# Function to insert a new company info entry
def insert_company_info(ticker, name, sector, industry, website, description):
    connection = create_connection()
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO company_info (ticker, name, sector, industry, website, description)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    
    values = (ticker, name, sector, industry, website, description)
    cursor.execute(insert_query, values)
    
    connection.commit()
    
    print(f"Company {name} inserted successfully.")
    
    cursor.close()
    connection.close()

insert_company_info(
    ticker="AAPL4",
    name="Samsung",
    sector="Technology",
    industry="Consumer Electronics Test",
    website="https://www.samsung.com",
    description="Sexy designs, manufactures, and markets mobile devices, consumer electronics, and digital services."
)