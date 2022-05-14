a=list(map(int,input().split()))
b=list(set(a))
b.sort() 
c=[]
for i in range(len(a)//2):
	c.append(b[0])
	c.append(b[-1])
	b.pop(0)
	b.pop(-1) 
if len(a)%2==0:
	print(c)
else:
	c.extend(b)
	print(c)
