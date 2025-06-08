import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="Alpana@1604")

print(mydb,"Connection Establisted....")