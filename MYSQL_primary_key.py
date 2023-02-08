import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password="root",
    database="demo1"
)

mycursor = con.cursor()
# to create a prmiary key if the table does not exist already

'''mycursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), qualification VARCHAR(30))")'''

# if the table exist already then use the following command

mycursor.execute("ALTER TABLE student ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
