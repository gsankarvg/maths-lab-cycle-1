# print a lower triangular matrix and upper triangular matrix.
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

lower_triangle = np.tril(matrix1)
print("lower triangle is ",lower_triangle)
upper_triangle = np.triu(matrix1)
print("upper triangle is ",upper_triangle)

