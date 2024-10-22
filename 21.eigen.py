import numpy as np

matrix = np.array([[4, -2],
                   [1, 1]])

a = np.random.randint(0, 10, size=(3, 3))
eigenvalues, eigenvectors = np.linalg.eig(a)

print("Matrix:")
print(a)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)



