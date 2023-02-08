import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="demo1"
)

mycursor = con.cursor()

# here we are going to create a table

mycursor.execute("CREATE TABLE student (name VARCHAR(30), role VARCHAR(30))")

# To see the tables in the database

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
