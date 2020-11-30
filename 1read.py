with open("1nik.txt","r") as file:
    x=file.read()
    x=x.split()
    for i in x:
        print(i,end="")
        print("#",end="")