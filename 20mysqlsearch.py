import mysql.connector as mycon
myco=mycon.connect(host="localhost",user="root",passwd="root",database="why")
cursor=myco.cursor()
cursor.execute("select * from school")
print("Before deleting",cursor.fetchall())
x=int(input("Enter the roll number to search"))

cursor.execute("select * from school where rn=%s",(x,))
print("deleting",cursor.fetchall(),".........")
cursor.execute("delete from school where rn=%s",(x,))
myco.commit()
print("deleted")
cursor.execute("select * from school")
print("after deleting",cursor.fetchall())