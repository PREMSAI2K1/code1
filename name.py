a=input().split(" ") 
print(a)
b=[]
final_str=""
for i in a:
    c=i.split(":")
    d=c[0]
    e=c[1]
    name_length=len(c) 
    
    max=0 
    for digit in e:
        if(int(digit)<=name_length):
            if(max<int(digit)):
                max=int(digit) 
    if(max==0):
        final_str+='X'
    else:
        final_str+=d[max-1]
print(final_str)


