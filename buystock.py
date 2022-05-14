prices=list(map(int,input().split()))
max=0 
j=0
for i in range(1,len(prices)):
	sum=prices[i]-prices[j] 
	if sum > max:
		max=sum 
	if prices[i] < prices[j]:
		j=i  
print(max) 

'''prices=[7,1,5,3,6,4]
a=min(prices) 
max=a 
for i in range(len(prices)):
    if prices[i]==a:
        for j in range(i+1,len(prices)):
            if prices[j]>max:
                max=prices[j] 
                
print(max-a)
        
'''