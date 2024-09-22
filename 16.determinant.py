# find the determinant of a matrix.
import numpy as np

n = int(input("Enter the size of the square matrix (n x n): "))
matrix = []
print(f"Enter the elements of the {n}x{n} matrix row by row:")
for i in range(n):
    row = list(map(int, input(f"Enter row {i+1} (space-separated): ").split()))
    matrix.append(row)
matrix = np.array(matrix)

deter = np.linalg.det(matrix)
print("determinant is :\n",deter)