#create database
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Arshdeep@12345")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE school;")

