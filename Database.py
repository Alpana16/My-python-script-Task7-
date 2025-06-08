import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="Alpana@1604")
db_cursor=mydb.cursor()

db_cursor.execute("create database LearnCoding")

print("Database Created !!")