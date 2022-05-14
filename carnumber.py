t=int(input())
for i in range(t):
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))[:a[0]]
	c=list(map(int,input().split()))[:a[0]]
	e=a[1]
	d=[]
	sum=0
	if e%2==0:
		for i in range(len(b)):
			if b[i]%2!=0:
				sum=sum+c[i]
				
	else:
		for i in range(len(b)):
			if b[i]%2==0:
				sum=sum+c[i]
	print(sum)

