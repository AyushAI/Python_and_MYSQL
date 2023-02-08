import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="root",
    database="demo1"
)

mycursor = con.cursor()

sql = "INSERT INTO student (name,role) VALUES (%s,%s)"
val = [
    ("Atharva","AI Engineer"),
    ("Vaishali","Teacher"),
    ("Rahul","BSC Agriculture"),
    ("Jayant","Collector"),
    ("Tanmay","BCA"),
    ("Ikshit","AI Engineer"),
    ("Anand","Teacher")
]

'''
To insert multiple rows into a table, use the executemany() method.
The second parameter of the executemany() method is a list of tuples,
containing the data you want to insert:
'''
mycursor.executemany(sql,val) 
# here you need to use insertmany() method to insert multiple records into the databse

con.commit()

'''Notice the statement: con.commit().
It is required to make the changes, otherwise no changes are made to the table'''

print(mycursor.rowcount, "record inserted successfully")
