s=input()
c=s.strip(" ")
print(c)

a=c.lower()
print(a)
b=set() 
for i in range(len(a)):
	if a[i].isalpha():
		b.add(a[i])  
print(b)
if len(b)==26:
	print("it contains all alphabets")
else:
	print("no")

