from pickle import*
with open("3nikbn.dat","wb") as file:
    x=[]
    while True:
        name=input("entre the name")
        rn=int(input("enter the roll no"))
        dic={"name":name,"rollno":rn}
        y=input("enter y to cont n to not")
        x.append(dic)
        if y=="n":
            break
    dump(x,file)    
with open("3nikbn.dat","rb") as file1:
    red=load(file1)
    print(red)
    
check=int(input("enter the the roll no to check"))
for i in red:
    if int(i["rollno"])==int(check):
        print(i["name"],end="")
        print(" has roll number ",i["rollno"])
