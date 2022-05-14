n1=['python','flask','django','tkinter']
n2=n1 
n3=n1[:2] 
print(n3) 
n2[0]='scipy'
n3[1]='numpy'
print(n2)
print(n1) 
print(n3) 
s=10 
for i in (n1,n2):
    if i[0]=="python":
        s=s+1 
    if i[1]=='python':
        s=s+2 
print(s)        