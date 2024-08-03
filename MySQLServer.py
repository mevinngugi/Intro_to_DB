import mysql.connector

try:
    # Database connection details (replace with your own)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Your Password",
        # database="mydb"
    )
    
    mycursor = mydb.cursor()
    create_db = mycursor.execute("""
        CREATE DATABASE IF NOT EXISTS alx_book_store
    """)
    print("Database 'alx_book_store' created successfully!")
    mydb.close()

    print("Database connection closed.")
except mysql.connector.Error:
    print("Failed to connect to the DB")
