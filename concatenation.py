l=[3,2,6,5,1,4,8,9] 
a,b=input().split()
a=int(a)
b=int(b)
c=l.index(a)
d=l.index(b)
print(c)
print(d)
e=0
for i in range(len(l)):
    if i>=3 and i<=6:
        continue 
    e=e+l[i] 
print(e) 
d=[str(l[i]) for i in range(c,d+1)]
f=''.join(d)
print(f)
g=int(f)
print(e+g)