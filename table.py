import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="Alpana@1604",database="LearnCoding")
db_cursor=mydb.cursor()
db_cursor.execute("show tables")
for i in db_cursor:
   print(i)