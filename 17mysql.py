import mysql.connector as mycon
myco=mycon.connect(host="localhost",user="root",passwd="root",database="why")
cursor=myco.cursor()
cursor.execute("select* from emp")
x=cursor.fetchall()
print(x)