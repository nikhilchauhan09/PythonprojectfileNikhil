def sum4():
    n=int(input("THE NUMBER OF ELEMENTS OF 1 - 2 + 3 - 4 + 5 - 6 + 7 - ..... + n  : "))
    sum=0
    show=""
    for i in range(1,n+1):
        sum+=((-1)**(i-1))*i
        if i==1:
            show+=f"{((-1)**(i-1))*i} "
        else:
            show+=f" +{((-1)**(i-1))*i} "
    print(f"{show} == {sum}")
while True:
    sum4()
    y=input("y to continue n to exit ")
    if y=="n":
        break