stack=[]
x="1:add element,2:pop element,0: to exit"
while True:
    y=input(x)
    if y=="0":
        print(stack)
        break
    if y=="1":
        stack.append(input("add element at last"))
        print(stack)
    if y=="2":
        stack.pop()
        print(stack)
