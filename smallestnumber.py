n=int(input())
k=9
a=[]
if n<10:
    print(10+n)
else:
    while k>1:
        if n%k==0:
            a.append(str(k))
            n=n//k 
        else:
            k=k-1
    b=a[::-1]
    print(''.join(b))