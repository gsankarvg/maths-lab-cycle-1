import numpy as np

r1 = int(input("enter the number of rows of  matrix 1 : "))
c1 = int(input("enter the number of columns of  matrix 1: "))
matrix1 = []
for i in range(r1):
    row = []
    for j in range(c1):
        item = int(input("enter the element: "))
        row.append(item)
    matrix1.append(row)

r2 = int(input("enter the number of rows of  matrix 2 : "))
c2 = int(input("enter the number of columns of matrix 2: "))

matrix2 = []
for i in range(r2):
    row = []
    for j in range(c2):
        item = int(input("enter the element: "))
        row.append(item)
    matrix2.append(row)

a = np.array(matrix1)
b = np.array(matrix2)
print("matrix 1 is \n",a)
print("matrix 2 is \n",b)
difference = a - b
sum = a + b
print("sum of the matrices is \n",sum)
print("difference of the matrices is \n",difference)
