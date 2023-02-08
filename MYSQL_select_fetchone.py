import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="root",
    database = "demo1"
)

mycursor = con.cursor()
mycursor.execute("SELECT * FROM student")

'''
If you are only interested in one row, you can use the fetchone() method.
The fetchone() method will return the first row of the result:
'''
myresult = mycursor.fetchone()
print(myresult)