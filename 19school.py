import mysql.connector as mycon
myco=mycon.connect(host="localhost",user="root",passwd="root",database="why")
cursor=myco.cursor()
cursor.execute("select * from school")
print(cursor.fetchall())
x=int(input("Enter the roll number to search"))
cursor.execute("update school set name=%s,rn=%s where rn=%s",(str(input("Enter the updated name")),int(input("enter the updated roll number")),x))
myco.commit()
cursor.execute("select * from school")
print(cursor.fetchall())
