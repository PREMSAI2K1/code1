s=input()
a=s.replace('53','')
print(a) 
b=a.replace('8','')
print(b) 
if b.isalnum():
	print(b.lower()) 
else:
	print("invallid input given")