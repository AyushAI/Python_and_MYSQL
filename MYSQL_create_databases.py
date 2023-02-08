import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

mycursor = con.cursor()

# here we are creating a database
mycursor.execute("CREATE DATABASE demo1")

# to check if the database exist or not
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)