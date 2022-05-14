l=[1,2,3,4,5,6]
sum=6 
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==sum:
            print(l[i],l[j])