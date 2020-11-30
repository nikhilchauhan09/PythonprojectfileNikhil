n=int(input("the number of elements to add"))
x=[]
for i in range(n):
    x1=int(input("enter the element to add"))
    x.append(x1)
print(x)
for i in range(0,len(x),2):
    try:
        x[i],x[i+1]=x[i+1],x[i]
    except:
        IndexError
        break 
print(x)
    