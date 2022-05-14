def fib(n):
	a=0
	b=1
	if n==0:
		return 0
	if n==1:
		return 1
	else:
		print(a,end=" ")
		print(b,end=" ")
		for i in range(2,n+1):
			c=a+b
			a=b 
			b=c 
			print(c,end=" ") 
fib(9)