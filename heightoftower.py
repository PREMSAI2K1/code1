t=int(input())
for i in range(t):
    x=int(input())
    y=list(map(int,input().split()))[:x]
    a=y[0]
    count=1 
    for i in range(1,x):
        if y[i]>a:
            count=count+1 
            a=y[i]
    print(count)