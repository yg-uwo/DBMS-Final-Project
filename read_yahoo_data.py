import yahoo_fin
from db_connector import create_connection 
connection = create_connection()
cursor = connection.cursor()



def add_company_info():
    print("G6TFGYSU")



connection.commit()
cursor.close()
connection.close()
