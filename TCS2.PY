n=int(input())
a=list(map(int,input().split()))[:n] 
c=[]
for i in range(len(a)-2):
	for j in range(i+1,len(a)-1): 
		print(a[i],a[j],a[j+1])
		b=a[i]+a[j]+a[j+1] 
		c.append(b) 
e=max(c)
print(e)


