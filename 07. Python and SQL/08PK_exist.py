#Primary key in existing tables
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Arshdeep@12345", database = "school")

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE student ADD COLUMN id int(10) AUTO_INCREMENT PRIMARY KEY")
