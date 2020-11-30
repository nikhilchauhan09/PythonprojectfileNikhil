queu=[]
x="1:add element,2:pop element,0: to exit"
while True:
    y=input(x)
    if y=="0":
        print(queu)
        break
    if y=="1":
        queu.append(input("add element at last"))
        print(queu)
    if y=="2":
        queu.pop(0)
        print(queu)