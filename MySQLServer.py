from mysql.connector import Error

import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (update user and password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Update with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                print(f"Error creating database: {e}")
            finally:
                cursor.close()
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()