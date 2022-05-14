n=int(input())
m=int(input())
a=[0]*m
a[n-1]=1 
for i in range(n,m):
    for j in range(i-n,i):
        a[i]=a[i]+a[j] 
for i in range(m):
    print(a[i],end=" ")