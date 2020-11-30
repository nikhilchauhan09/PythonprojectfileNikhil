def dostr():
    x=input("Enter the string")
    y=int(input("1:Capitalize,2:Casefold,3:Count,4:SwapCase,5:Split,6:Title"))
    if y==1:
        print(x.capitalize())
    if y==2:
        print(x.casefold())
    if y==3:
        z=input("Enter charecter to search")
        print(x.count(z))
    if y==4:
        print(x.swapcase())
    if y==5:
        print(x.split())
    if y==6:
        print(x.title())
while True:
    dostr()
    y=input("y to continue n to exit ")
    if y=="n":
        break
