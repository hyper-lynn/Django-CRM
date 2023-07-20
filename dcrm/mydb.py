import mysql.connector



dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
)

#prepare the cursor object
cursorObject = dataBase.cursor()

#create database 
cursorObject.execute("CREATE DATABASE blackcat")

print("ALL done")