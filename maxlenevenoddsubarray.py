a=[5,10,20,6,3,8]
res=1
for i in range(len(a)):
    cur=1
    for j in range(i+1,len(a)):
        if (a[j]%2==0 and a[j-1]%2!=0) or (a[j]%2!=0 and a[j-1]%2==0):
            cur=cur+1 
        else:
            break 
    res=max(res,cur)
print(res)
        