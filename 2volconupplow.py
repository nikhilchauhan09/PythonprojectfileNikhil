cv,cc,cu,cl=0,0,0,0
with open("1nik.txt","r") as file:
    x=file.read()
    for i in x:
        if i.upper() in ["B",'C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']:
            cc+=1
        if i.upper() in ["A","E","I","O","U"]:
            cv+=1 
        if i.upper()==i and i.upper() in ["A","E","I","O","U","B",'C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']:
            cu+=1
        if i.lower()==i and i.upper() in ["A","E","I","O","U","B",'C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']:
            cl+=1
    print(f"THE NUMBER OF VOWELS ARE : {cv}")
    print(f"THE NUMBER OF CONSONANTS ARE : {cc}")
    print(f"THE NUMBER OF uppercase charecter ARE : {cu}")
    print(f"THE NUMBER OF lowercase charecter ARE : {cl}")