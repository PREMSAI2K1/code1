n=int(input())
l=[]
for i in range(n):
	x=int(input())
	l.append(x) 
max=l[0]
count=1	
for i in range(1,n):
	if l[i]>max:
		count=count+1
		max=l[i] 
print(count)		
