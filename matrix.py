n=int(input()) #square matrix
matrix=[]
for i in range(n):
	a=[]
	for j in range(n):
		x=int(input())
		a.append(x)
	matrix.append(a) 
print(matrix)
for i in range(n):
	for j in range(n):
		print(matrix[i][j],end=" ")
	print() 
suml=0
sumr=0
i=0
j=0
while(i!=n and j!=n):
	suml=suml+matrix[i][j]
	i=i+1
	j=j+1 
i=0
j=n-1
while(i!=n and j!=n):
	sumr=sumr+matrix[i][j]
	i=i+1
	j=j-1
print(abs(suml-sumr)) #difference between diagonals
