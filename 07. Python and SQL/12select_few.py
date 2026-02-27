import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Arshdeep@12345", database = "school")

mycursor = mydb.cursor()
mycursor.execute("SELECT name, age FROM student")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)