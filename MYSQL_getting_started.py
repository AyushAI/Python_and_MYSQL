# at first install the mysql workbench new version 
# and then open command prompt and type the following command
# pip install mysql-connector-python

import mysql.connector

#now create a connection with the database

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

print(con)