# extract the diagonal vector from matrix and create diagonal matrix from vector.
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

diagonal_vector = np.diag(matrix1)
print("diagonal vector : ",diagonal_vector)
diagonal_matrix = np.diag(diagonal_vector)
print("diagonal matrix : \n",diagonal_matrix)


