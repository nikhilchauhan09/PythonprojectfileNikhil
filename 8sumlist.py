def sumlis(l):
    s=0
    for i in l:
        s+=i
    return(s)
while True:
    x=input("Enter the data in form of list or tuple ").split()
    for i in range(len(x)):
        x[i]=int(x[i])
    
    print(sumlis(x))
    y=input("y to continue n to exit ")
    if y=="n":
        break