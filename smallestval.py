n=int(input()) #to find the smallest integer value of b for a given value of a.
i=9            #if we multiply the digits of b,we should get exact value of a.
a=[]
while(n>=1 and i>=2):
    r=n%i
    if r==0:
        n=n//i
        a.append(str(i))
        i=i+1
        
    else:
        i=i-1
if n==1:
    b=a[::-1]
    c=''.join(b)
    print(int(c))
    
        
    