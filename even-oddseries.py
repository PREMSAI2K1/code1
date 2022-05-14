s=input()
character=[]
even=[]
odd=[] 
res=[]
for i in s:
	if i.isdigit():
		if int(i)%2==0:
			even.append(i)
		else:
			odd.append(i) 
	else:
		character.append(i) 
char=len(character)
a=min(len(even),len(odd))
if char%2==0:
	for i in range(a):
		res.append(odd.pop(0))
		res.append(even.pop(0))
	res.extend(even)
	res.extend(odd) 
else:
	for i in range(a):
		res.append(even.pop(0))
		res.append(odd.pop(0))
	res.extend(even)
	res.extend(odd)
b=''.join(res)
print(b)