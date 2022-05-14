'''For a given list of numbers, find its factors and add the factors. Then if the sum of factors is present in the original list, sort it and print it.'''

l=[28,6,2,12,1]
b=[]
for i in l:
    a=[]
    for j in range(1,i//2+1):
        if i%j==0:
            a.append(j) 
            
    b.append(sum(a)) 
c=[]
for i in b:
    if i in l:
        c.append(i)
c.sort()
for i in c:
    print(i,end=" ")  




    