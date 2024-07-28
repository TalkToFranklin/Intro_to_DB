import mysql.connector

mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Franklinakinopeoluwa@2020",
    database = "alx_book_store"
)

mycursor = mydatabase.cursor()
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print (i)