'''Valid Hexadecimal Representation of Number'''
s=input()
i=0
for i in range(len(s)):
    if (s[i]<'0' or s[i]>'9') and (s[i]<'A' or s[i]>'F'):
        print("no")
        
        
        
        
print("yes")
        