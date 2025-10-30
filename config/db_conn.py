import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()
connection=None
    
def create_connection():
        global connection
        if connection and connection.is_connected():
         return connection
            
        try:
            connection=mysql.connector.connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_NAME'),
                charset=os.getenv('CHARSET')
            )
            
            if connection.is_connected():
                  print('connection was successfully established')
                  return connection
            

        except Error as e:
            print(f"Database connection failed: {e}")
            return None
def close_connection():
     global connection
     if connection and connection.is_connected:
          print('Connection closed')
          return connection

if __name__ == '__main__':
    create_connection() 
    close_connection()      
    
    
