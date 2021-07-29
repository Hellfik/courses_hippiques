import mysql.connector
from mysql.connector import Error
import pandas as pd

class Database:
    connection = None

    def __init__(self, host_name, user_name, user_password, db_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.db_name = db_name
    
    def db_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host_name,
                user = self.user_name,
                password = self.user_password,
                database = self.db_name
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return self.connection

    def read_query(self,connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")

    def build_dataframe(self, connection, query):
        df = pd.read_sql(query, connection)
        return df

    def disconnect_db(self):
	    self.connection.close()	# Disconnect
	    print('Succesfully disconnected.')
