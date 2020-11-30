import csv
x=["NAME","ROLL NUMBER"]

with open("1nik.csv","w") as file:
    wr=csv.writer(file)
    wr.writerow(x)
    while True:
        name=input("enter name ")
        rn=int(input("enter roll number "))
        lm=[name,rn]
        wr.writerow(lm)
        y=input("enter y to continue n to not")
        if y=="n":
            break
with open("1nik.csv","r") as file1:
    reader=csv.reader(file1)
    
    while True:
        x=0
        rnin=int(input("enter roll number to search"))
        for row in reader:
            if len(row)!=0:
                if row[1]==str(rnin):
                    print("the name is ",row[0])
                    x=1
        if x==0:
            print("Not found of this particulars")
        y=input("y to continue n to not")
        if y=="n":
            break
