s=int(input())
if s<0:
	print("valid number")
else:
	a=str(s)
	sum=1
	for i in a:
		sum=sum*int(i) 
	print(sum)

