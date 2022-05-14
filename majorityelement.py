a=[8,7,6,8,6,6,6,6]
b=len(a)
#majority-element=the element repeated more than n/2 times in array 
for i in range(len(a)):
    count=1
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            count=count+1
    if count>b//2:
        print(i)   #index of element
        break 