def find_max(lis):
    print(f"the maximum is {max(lis)}")
    print(f"the minimum is {min(lis)}")
while True:
    x=input("Enter the data in form of list or tuple ").split()
    for i in range(len(x)):
        x[i]=int(x[i])
    
    find_max(x)
    y=input("y to continue n to exit ")
    if y=="n":
        break