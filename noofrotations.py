N=int(input())
b=list(map(str,input().split()))[:N]
a=b[0] #original string
count=0
for i in range(1,len(b)):
    if b[i]==a:
        continue
    else:
        while True:
             b[i]=b[i][1:]+b[i][0:1] #slicing by rotating one element and checking
             if b[i]==a:
                 count=count+1 
                 break 
             else:
                 count=count+1 
print(count)