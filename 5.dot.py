# matrix dot product.
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

r2 = int(input("enter the no of rows of matrix1: "))
c2 = int(input("enter the no of cols of matrix1: "))
m2 = []
for i in range(r2):
    row = []
    for j in range(c2):
        element = int(input("enter the element: "))
        row.append(element)
    m2.append(row)
matrix2 = np.array(m2)

if c1!=r2:
    print("dot product not possible")
else:
    dot_product = np.dot(matrix1,matrix2)
    print("result = \n",dot_product)
