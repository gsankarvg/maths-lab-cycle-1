# create an identity matrix.
import numpy as np

n = int(input("enter the size of the identity matrix: "))
id = np.identity(n)
print("identity matrix : \n",id)
