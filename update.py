import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="Alpana@1604",database="LearnCoding")
db_cursor=mydb.cursor()
db_Updatedata="update LearnCoding.Emp set roll=%s where Ename=%s"
db_value=(50,"Rohit")
db_cursor.execute(db_Updatedata,db_value)
mydb.commit()
print(db_cursor.rowcount,"Data Updated!!!")