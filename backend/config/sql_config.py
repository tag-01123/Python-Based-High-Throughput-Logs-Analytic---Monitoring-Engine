import mysql.connector
from mysql.connector import Error

def get_sql():
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="",
        port=3306
    )
        if connection.is_connected():
            print("Connection successful!!")
            return connection
        else:
            print("Unable to connect!!")

    except Error as e:
        return (f"Error: {e}")

get_sql()