a='onlinestudy'
b=''
for i in range(len(a)):
    c=ord(a[i])
    d=ord('a')-c+ord('z')
    b=b+chr(d) 
print(b)
    