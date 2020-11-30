def sum1():
    n=int(input("THE NUMBER OF ELEMENTS OF 1 + x + x2 + x3 + x4 + ..... + xn: "))
    X=int(input("THE VALUE OF X: "))
    sum=0
    show=""
    for i in range(n):
        sum+=X**i
        if i==0:
            show+=f"({X}**{i}) "
        else:
            show+=f" + ({X}**{i}) "
    print(f"{show} == {sum}")
while True:
    sum1()
    y=input("y to continue n to exit ")
    if y=="n":
        break
