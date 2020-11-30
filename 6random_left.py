import random
def ra():
    print(f"the number on dice is {random.randrange(1,7)}")
while True:
    ra()
    y=input("y to continue n to exit ")
    if y=="n":
        break