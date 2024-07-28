import mysql.connector
from mysql.connector import Error

def create_database():
    """Create a MySQL database named 'alx_book_store'."""
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host ='localhost',  # MySQL server host 
            user ='root',  # MySQL username
            password='Franklinakinopeoluwa@2020'  # MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
