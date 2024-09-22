# write a program to create two numpy arrays of random integers between zero and twenty of shape (dimension)
# 3x3 and perform matrix addition, multiplication and transpose of the product matrix.
import numpy as np

matrix1 = np.random.randint(0,21,size=(3,3))
matrix2 = np.random.randint(0,21,size=(3,3))
print("matrix 1 = \n",matrix1)
print("matrix 2 = \n",matrix2)

add_matrix = np.add(matrix1,matrix2)
print("matrix addtion: \n",add_matrix)

product_matrix = np.dot(matrix1,matrix2)
print("matrix multiplication = \n",product_matrix)

transpose_product = np.transpose(product_matrix)
print("transpose of product matrix : \n",transpose_product)


