a=int(input())
b=int(input())
d=[]
for i in range(a,b+1):
	c=str(i)
	for j in c:
		d.append(j) 
for i in d:
	if d.count(i)==1:
		print(i,end=" ") 







		