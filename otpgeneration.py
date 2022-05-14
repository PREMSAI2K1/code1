n=int(input())
a=str(n)
b=list(a)
c=[]
f=[]
for i in range(len(b)):
    if i%2!=0:
        c.append(int(b[i]))
for i in c:
    d=i*i 
    f.append(str(d))
print(f)
e=''.join(f) 
for i in range(0,4):
    print(e[i],end="")
    