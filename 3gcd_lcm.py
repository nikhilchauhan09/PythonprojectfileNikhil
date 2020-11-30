def gcde(x,y):
    if y==0:
        return x
    else:
        return gcde(y,x%y)
def lcme(x,y):
    lcm=x*y/gcde(x,y)
    print(f"THE LCM OF {x} AND {y} IS {lcm}")
while True:
    x=int(input("Enter the 1st Number :"))
    x2=int(input("Enter the 2nd Number :"))
    print(f"THE GCD OF {x} AND {x2} IS IS {gcde(x,x2)}")
    lcme(x,x2)
    y=input("y to continue n to exit ")
    if y=="n":
        break