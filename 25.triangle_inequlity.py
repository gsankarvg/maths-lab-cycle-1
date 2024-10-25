# Program to show the inequality of two vectors.

import numpy as np

v1 = list(map(int, input("Enter the first vector, separated by space: ").split()))
v2 = list(map(int, input("Enter the second vector, separated by space: ").split()))

norm_v1 = np.linalg.norm(v1)
norm_v2 = np.linalg.norm(v2)
norm_sum = np.linalg.norm(np.add(v1, v2))

# Check the triangle inequality
if norm_sum <= norm_v1 + norm_v2:
    print("|| v1 + v2 || <= || v1 || + || v2 || (Triangle inequality holds)")
else:
    print("|| v1 + v2 || > || v1 || + || v2 || (Triangle inequality does not hold)")
