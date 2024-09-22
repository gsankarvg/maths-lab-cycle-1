# create a matrix of ones with the given dimension.
import numpy as np
dim = input("enter the dimensions in rxc format: ")
r,c = map(int,dim.split("x"))

matrix = np.ones((r,c))
print(matrix)
