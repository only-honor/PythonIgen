import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Arshdeep@12345', database = 'school')

mycursor = mydb.cursor()
sql = "DELETE FROM student WHERE id = 303"
mycursor.execute(sql)

mydb.commit()
print(mycursor.rowcount, "Record Deleted")