n=input()
s=list(n)
i=0
while (i<len(s)-2):
    if s[i]==s[i+1]:
        s.remove(s[i]) 
        i=i+0
    else:
        i=i+1    
print(s)