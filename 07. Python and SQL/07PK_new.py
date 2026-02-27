#Primary Key in new table

import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Arshdeep@12345", database = "school")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE teacher(id int(10) auto_increment primary key, name varchar(20), age int(10), salary int(10))")
