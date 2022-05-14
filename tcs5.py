a=list(map(int,input().split()))
sum=a[0]
b=[]
for i in range(1,len(a)):
	if a[i]>a[i-1]:
		sum+=a[i] 
	else:
		b.append(sum)
		sum=a[i] 
b.append(sum)
print(b)
