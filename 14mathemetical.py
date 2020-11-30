import math
x="1:sqrt,2:factorial,3:gcd,4:lcm,5:trig,6:log,0:exit"
while True: 
    y=int(input(x))
    if y==0:
        break
    if y==1:
        print(math.sqrt(int(input("enter the number to find square root"))))
    if y==2:
        print(math.factorial(int(input("enter the number to find factorial"))))
    if y==3:
        print(math.gcd(int(input("enter the 2nd number")),int(input("enter the 1st number"))))
    if y==4:
        print(math.lcm(int(input("enter the 2nd number")),int(input("enter the 1st number"))))
    if y==5:
        z=int(input("the degrees to find trig  functions"))
        print(math.sin(math.radians(z)),math.cos(math.radians(z)),math.tan(math.radians(z)),)
    if y==6:
        print(math.log(int(input("enter the number")),int(input("enter the base"))))

