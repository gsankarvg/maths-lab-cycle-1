# 1. create a matrix using numpy.
import numpy as np
r = int(input("enter the number of rows: "))
c = int(input("enter the number of columns: "))
matrix = []

for i in range(r):
    row = []
    for j in range(c):
        item = int(input("enter the element: "))
        row.append(item)
    matrix.append(row)
a = np.array(matrix)

print("the matrix is \n",a)
