# perform matrix division with the help of numpy arrays.

import numpy as np

n1 = int(input("Enter the size of the square matrix (n x n): "))
mat1 = []
print(f"Enter the elements of the {n1}x{n1} matrix row by row:")
for i in range(n1):
    row = list(map(int, input(f"Enter row {i+1} (space-separated): ").split()))
    mat1.append(row)
matrix1 = np.array(mat1)

n2 = int(input("Enter the size of the square matrix (n x n): "))
mat2 = []
print(f"Enter the elements of the {n2}x{n2} matrix row by row:")
for i in range(n2):
    row = list(map(int, input(f"Enter row {i+1} (space-separated): ").split()))
    mat2.append(row)
matrix2 = np.array(mat2)

matrix2_inv = np.linalg.inv(matrix2)

result = np.dot(matrix1,matrix2_inv)

print("result = \n ",result)

