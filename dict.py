d={}
n=int(input())
for i in range(n):
    k=input("key:")
    v=input("value:")
    d[k]=v 
print(d) 
key=input()
value=input()
d.update({key:value})   
print(d)
key1=input() 
if key1 in d.keys():
	print("key is already present")
else:
	print("not present")	