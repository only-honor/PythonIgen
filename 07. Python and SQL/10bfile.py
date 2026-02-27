#insert values
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Arshdeep@12345", database = "school")

mycursor = mydb.cursor()


sql = "INSERT INTO student(name, rollnum, age, class, section, id) VALUES (%s, %s, %s,%s, %s, %s)"
val = ("Bob", 3, 15, 7, "A", 303)

mycursor.execute(sql, val)
mydb.commit() #Reqd. to commit changes

print(mycursor.rowcount, "Record Inserted")
print("Record Inserted, ID: ", mycursor.lastrowid)
