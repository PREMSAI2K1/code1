n=int(input())
a=str(n)
l=[]
for i in a:
    l.append(int(i)) 
l.sort()
for i in l:
    print(i,end="")
    