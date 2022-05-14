a=[1,2,1,3,4,3,3]
k=int(input())
for i in range((len(a)-k)+1):
    b=len(list(set(a[i:i+k])))
    print(b,end=" ")