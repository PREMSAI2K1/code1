a=[5,7,3,9,8,2]
for i in range(len(a)-1):
	for j in range(len(a)-1):
		if a[j]>a[j+1]:
			temp=a[j]
			a[j]=a[j+1]
			a[j+1]=temp
print(a)