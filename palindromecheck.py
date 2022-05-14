n=int(input())
a=str(n)
b=a[::-1]
a=int(a)
b=int(b)
if(a+b<=9):
    print(a+b)
while(a+b>=9):
  c=a+b 
  d=str(c)
  if d==d[::-1]:
    print(int(d))
    break
  else:
    e=d 
    f=e[::-1]
    a=int(e)
    b=int(f)