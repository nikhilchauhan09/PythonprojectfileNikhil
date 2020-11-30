
def counter():
    cv,cc,cu,cl=0,0,0,0
    x=input("Enter the string")
    for i in x:
        if i.upper() in ["B",'C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']:
            cc+=1
        if i.upper() in ["A","E","I","O","U"]:
            cv+=1 
        if i.upper()==i:
            cu+=1
        if i.lower()==i:
            cl+=1
    print(f"THE NUMBER OF VOWELS ARE : {cv}")
    print(f"THE NUMBER OF CONSONANTS ARE : {cc}")
    print(f"THE NUMBER OF uppercase charecter ARE : {cu}")
    print(f"THE NUMBER OF lowercase charecter ARE : {cl}")

while True:
    counter()
    y=input("y to continue n to exit ")
    if y=="n":
        break
