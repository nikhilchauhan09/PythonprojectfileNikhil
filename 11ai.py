with open("1nik.txt","r") as file:
    x=file.read()
x=x.split()
y=[]
for i in x:
    y.append([i,x.count(i)])
z=[]
for i in y:
    if i not in z:
        z.append(i)
print("#"*34)
print("#"*34)
y=z
print(y)
for i in y:
    if i[1]>=3:
        print(i[0],i[1])


