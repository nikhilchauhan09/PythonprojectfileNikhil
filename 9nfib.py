def fibn(n):
    if n<=0:
        return "not possible"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibn(n-1)+fibn(n-2)
while True:
    x=int(input("Enter the Number to Find Fibonacci: "))
    print(fibn(x))
    y=input("y to continue n to exit ")
    if y=="n":
        break