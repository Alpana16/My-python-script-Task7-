import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="Alpana@1604",database="LearnCoding")
db_cursor=mydb.cursor()
db_insert="insert into Emp(Roll,Ename) values(%s,%s)"
db_list=[(30,"Anish"),(40,"Altaf"),(40,"Rohit")]
db_cursor.executemany(db_insert,db_list)
mydb.commit()
print(db_cursor.rowcount,"Record inserted")