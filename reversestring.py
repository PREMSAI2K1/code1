s=list(input())
index=-1
for i in range(len(s)-1,0,-1):
    if s[i].isalpha():
        temp=s[i]
        while True:
            index=index+1 
            if s[index].isalpha():
                s[i]=s[index]
                s[index]=temp 
                break
print(s)