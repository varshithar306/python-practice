age = int(input("Enter your age: "))
name=(input("enter ur name"))
year=2026-age
print(f"hii {name}! You are {age} years old and were born in {year}")



c=input("enter a sentence")
z=c.upper()
y=c.count("a")
p=c.count("e")
d=c.count("i")
o=c.count("o")
f=c.count("u")
print(z)
print(y+p+d+o+f)
m=c.split(" ")
print(len(m))
for i in range(0,len(m)):
    print("m(i)")



alpha="abcdefghijklmnopqrstuvwxyz"
plain_text="examination"
key=5
for i in range(0,len(plain_text)):
    for j in range(0,len(alpha)):
        if alpha[j]==plain_text[i]:
            cyber=(j+key)%26
            print(alpha[cyber],end="")
            

#claude code
alpha="abcdefghijklmnopqrstuvwxyz"
plain_text="examination"
key=5
for i in range(0,len(plain_text)):
    k=alpha.find(plain_text[i])
    cyber=(k+key)%26
    print(alpha[cyber],end="")
