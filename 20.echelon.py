# print the echelon form of a matrix and find the rank.
import numpy as np
import sympy as sp

r1 = int(input("enter the no of rows of matrix1: "))
c1 = int(input("enter the no of cols of matrix1: "))
m1 = []
for i in range(r1):
    row = []
    for j in range(c1):
        element = int(input("enter the element: "))
        row.append(element)
    m1.append(row)
# Define a matrix
matrix = sp.Matrix(m1)

# Find row echelon form (rref stands for reduced row echelon form)
ref_matrix, pivot_columns = matrix.rref()

rank = matrix.rank()

print("Row Echelon Form (REF):")
sp.pprint(ref_matrix)

print("\nPivot columns:")
print(pivot_columns)

print("\nRank of the matrix:")
print(rank)
