import yahoo_fin
from db_connector import create_connection 
connection = create_connection()
cursor = connection.cursor()



cursor.execute("INSERT INTO Testing (symbol) VALUES (%s)", ("AAPL"))



connection.commit()
cursor.close()
connection.close()
