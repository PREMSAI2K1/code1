s=input()
l=[]
for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
        l.append(s[i:j]) 
print(l) 
length=0
for i in l:
    rev=i[::-1]
    if rev==i and len(i)>length:
        length=len(i)
        out=i 
print(out)         
