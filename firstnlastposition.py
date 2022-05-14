nums=[5,7,7,8,8,10]
target=8
b=[]
for i in range(len(nums)):
	if nums[i]==target:
		b.append(i) 
if len(b)==0:
	b.append(-1)
	b.append(-1)
	print(b)
elif len(b)==1:
	b.append(b[0])
	print(b)
elif len(b)>=2:
	a=[]
	a.append(b[0])
	a.append(b[-1])
	print(a)
																	