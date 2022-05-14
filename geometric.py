n=int(input())
for i in range(1,n+1):
    if(i%2!=0):
        if i==1:
            a=1 
        else:
            a=a*2  
    
    else:
        if i==2:
            b=1 
        else:
            b=b*3 
      
if(n%2!=0):
    print(a) 
else:
    print(b)

