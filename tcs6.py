a=input().split()
b=[]
c=[]
for i in range(len(a)):
	if a[i].isalpha():
		b.append(a[i])  
	if a[i].isdigit():
		c.append(a[i]) 
if len(a)>len(b)+len(c):
	print("invalid input")
print(b)
print(c)