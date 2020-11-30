def prime(x):
    for i in range(2,x):
        if x%i==0:
            print(f"{x} IS A COMPOSITE NUMBER")
            break
    else:
        print(f"{x} IS A PRIME NUMBER")
while True:
    x=int(input("Enter the Number to check wheter prime or not "))
    prime(x)
    y=input("y to continue n to exit ")
    if y=="n":
        break