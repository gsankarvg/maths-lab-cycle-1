import numpy as np

r1 = int(input("enter the no of rows of matrix 1 : "))
c1 = int(input("enter the no of columns of matrix 1 : "))
b = []
for i in range(r1):
    row = []
    for j in range(c1):
        item = int(input("enter the element: "))
        row.append(item)
    b.append(row)
matrix1 = np.array(b)
r2 = int(input("enter the no of rows of matrix 2 : "))
c2 = int(input("enter the no of columns of matrix 2 : "))

a = []
for i in range(r2):
    row = []
    for j in range(c2):
        item = int(input("enter the element: "))
        row.append(item)
    a.append(row)
matrix2 = np.array(a)
print(f"matrices you have entered is \n{matrix1} and \n{matrix2}")
print(f"Hadamard product of the matrices is \n{np.multiply(matrix1,matrix2)} ")


