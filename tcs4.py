s1=input()
s2=input() 
a=set()
for i in s1:
	if i in s2:
		a.add(i) 
b=list(a)
b.sort()
print(b)
b.reverse()
print(b)