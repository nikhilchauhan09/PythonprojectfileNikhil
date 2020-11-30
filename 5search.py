n=int(input("the number of elements to add"))
x=[]
for i in range(n):
    x1=int(input("enter the element to add"))
    x.append(x1)
def search():
    y=int(input("Element to search"))
    for i in range(len(x)):
        if y==x[i]:
            print(f"element is present at {i}")
while True:
    search()
    y=input("y to continue n to exit ")
    if y=="n":
        break