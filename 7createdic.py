n=int(input("the number of elements to add"))
x=[]
for i in range(n):
    name=input("name of student")
    marks=int(input("the marks"))
    rn=int(input("roll number"))
    dic={"rollno":rn,"name":name,"marks":marks}
    x.append(dic)
print("The following students have scored more than 75")
for i in x:
    if i["marks"]>75:
        print(i["name"],i["marks"])