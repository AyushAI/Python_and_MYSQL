import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="demo1"
)

mycursor = con.cursor()

mycursor.execute("SELECT * FROM student")

# We use the fetchall() method, which fetches all rows from the last executed statement.
myresult = mycursor.fetchall()

for x in myresult:
    print(x)