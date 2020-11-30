def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
while True:
    x=int(input("Enter the Number to Find Factorial: "))
    print(fact(x))
    y=input("y to continue n to exit ")
    if y=="n":
        break
