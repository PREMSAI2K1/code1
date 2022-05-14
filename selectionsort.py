a=[5,7,3,9,8,2]
for i in range(len(a)):
	min=i
	for j in range(i+1,len(a)):
		if a[j]<a[min]:
			min=j 
	if min!=i:
		temp=a[i]
		a[i]=a[min]
		a[min]=temp
print(a)

