s=input()
a=input()
b=[]
for i in s:
    if i not in a:
        b.append(i) 
for j in a:
    if j not in s:
        b.append(j)
print(b)