import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password="root",
    database = "demo1"
)

mycursor = con.cursor()
sql ="INSERT INTO student (name, role) VALUES (%s,%s)"
val = ("Ayush","AI Engineer")
mycursor.execute(sql, val)

con.commit()
'''Notice the statement: con.commit().
   It is required to make the changes, otherwise no changes are made to the table'''
print(mycursor.rowcount, "record inserted")