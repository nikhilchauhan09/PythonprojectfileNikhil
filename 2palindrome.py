x=input("Enter String to check")
x=x.lower()
y=""
for i in range(len(x)):
    y+=x[-(i+1)]
print(y)

if y==x:
    print("A PALINDROME")
else:
    print("not a  PALINDROME")
