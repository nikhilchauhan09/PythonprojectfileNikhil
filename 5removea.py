with open("5nikhello.txt","r") as file:
    x=file.readlines()
    for i in x:
        if "a" in i or "A" in i:
            x.remove(i)
with open("5nikhello1.txt","w") as file1:
    file1.writelines(x)
    print("done")
