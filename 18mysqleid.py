import mysql.connector as mycon
myco=mycon.connect(host="localhost",user="root",passwd="root",database="why")
cursor=myco.cursor()
cursor.execute("select * from emp where eid=%s",(int(input("Enter the employee number(eid) to check")),))
print(cursor.fetchall())
