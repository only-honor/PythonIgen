#
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Arshdeep@12345", database = "ToDo")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Tasks(id INT(10), name VARCHAR(20))")

