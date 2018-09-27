n=int(input("enter the value of rows n :"))
m=int(input("enter the value of coloumn m:"))
matrix  = []

for i in range(0,m):
	matrix.append([])
for i in range(0,n):
	for j in range(0,m):
		matrix[i].append(j)
		matrix[i][j]=0
for i in range(0,n):
	for j in range(0,m):
	 matrix[i][j] = input()
print(matrix)
