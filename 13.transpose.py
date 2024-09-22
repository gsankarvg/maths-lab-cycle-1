# find the transpose of a matrix.
import numpy as np

r1 = int(input("enter the no of rows of matrix1: "))
c1 = int(input("enter the no of cols of matrix1: "))
m1 = []
for i in range(r1):
    row = []
    for j in range(c1):
        element = int(input("enter the element: "))
        row.append(element)
    m1.append(row)
matrix1 = np.array(m1)
print("original matrix: \n",matrix1)
transpose = np.transpose(matrix1)
print("transpose is : \n",transpose)