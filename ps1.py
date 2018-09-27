n=int(input("enter the value of rows n :"))  #entering the number of rows and coloumns
m=int(input("enter the value of coloumn m:"))
matrix  = []

for i in range(0,m):       #entering the various elements of matrix from the user
	matrix.append([])
for i in range(0,n):
	for j in range(0,m):
		matrix[i].append(j)
		matrix[i][j]=0
for i in range(0,n):
	for j in range(0,m):
	 matrix[i][j] = input()
print(matrix)



for i in range(0,m):  #checking the different patterns in the matrix and accordingly printing the data
	for j in range(0,n):
		if matrix[i][j]=="S" :
			if  matrix[i-1][j]=="S" and matrix[i-2][j]=="S" and matrix[i+1][j]=="S" and matrix[i+2][j]=="S" and matrix[i][j+1]=="S" and matrix[i][j+2]=="S" and matrix[i][j-1]=="S" and matrix[i][j-2]=="S":
				print("9,5")
		
			elif  matrix[i-1][j]=="S" and matrix[i+1][j]=="S" and matrix[i][j-1]=="S" and matrix[i][j+1]=="S" :
				print("5,1")
		
		else:
			print("1")

