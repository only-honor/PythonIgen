#Create table
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Arshdeep@12345", database = "school")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE student(name varchar(20), rollnum int(20), age int(20), class int(10), section varchar(20))")

