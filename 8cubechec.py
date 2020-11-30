n=int(input("the number of elements to add"))
x=[]
for i in range(n):
    x1=int(input("enter the element to add"))
    x.append(x1)
print(x)
xnew=[]
for i in x:
    y=0
    for k in str(i):
        y+=int(k)**3
    if y==i:
        xnew.append(i)
print(max(xnew),min(xnew))

