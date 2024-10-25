import numpy as np
v1 = list(map(int, input("Enter the vector, separated by space: ").split()))
k = eval(input("enter the scalar: "))

a = np.multiply(np.linalg.norm(v1), abs(k))
b = np.linalg.norm(np.multiply(v1, k))
print(a,"\n", b)
if a == b:
    print(f" || k.u || = k.|| u || ( Linearity Holds ) ")
else:
    print(f" Linearity does not hold ")
