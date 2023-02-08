import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "demo1"
)

mycursor = con.cursor()
mycursor.execute("SELECT name FROM student")
myresult = mycursor.fetchall()

for rec in myresult:
    print(rec)