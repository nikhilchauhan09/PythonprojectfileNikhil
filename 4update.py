from pickle import*
with open("4nibn.dat","wb") as file:
    x=[]
    while True:
        name=input("entre the name")
        rn=int(input("enter the roll no"))
        marks=int(input("enter the marks"))
        dic={"name":name,"rollno":rn,"marks":marks}
        y=input("enter y to cont n to not")
        x.append(dic)
        if y=="n":
            break
    dump(x,file)
with open("4nibn.dat","rb") as file1:
    readx=load(file1)
    print(readx)
with open("4nibn.dat","wb") as file2:
    rnin=int(input("Enter the roll whose marks to change"))
    marksin=int(input("Enter marks to change"))
    for i in readx:
        if i["rollno"]==rnin:
            i["marks"]=marksin
    print(readx)
    dump(readx,file2)
