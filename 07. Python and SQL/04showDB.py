#show databases
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Arshdeep@12345")

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE school")

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)


