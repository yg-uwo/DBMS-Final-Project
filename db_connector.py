import mysql.connector
from dotenv import load_dotenv
# load_dotenv(dotenv_path='/.env.jot')
import os

load_dotenv()

# Function to create a connection to MySQL database
def create_connection():
    connection = mysql.connector.connect(
        host=os.getenv('HOST'),  # Use 'localhost' if no .env value found
        user=os.getenv('USERNAME'),      # Default to 'root'
        password=os.getenv('PASSWORD'),  # Replace with your password or use .env
        database=os.getenv('DBNAME') 
    )
    # Return connection object for later usage
    return connection

# Function to insert a new company info entry
def insert_company_info(ticker, name, sector, industry, website, description):
    connection = create_connection()
    cursor = connection.cursor()
    
    # Prepare the INSERT statement
    insert_query = """
    INSERT INTO company_info (ticker, name, sector, industry, website, description)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    
    # Values to insert into the table
    values = (ticker, name, sector, industry, website, description)
    
    # Execute the query
    cursor.execute(insert_query, values)
    
    # Commit the changes to the database
    connection.commit()
    
    print(f"Company {name} inserted successfully.")
    
    # Close the cursor and connection
    cursor.close()
    connection.close()

# Example of using the function
insert_company_info(
    ticker="AAPL4",
    name="Samsung",
    sector="Technology",
    industry="Consumer Electronics Test",
    website="https://www.samsung.com",
    description="Sexy designs, manufactures, and markets mobile devices, consumer electronics, and digital services."
)