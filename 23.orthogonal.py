import numpy as np

def are_orthogonal(vec_a, vec_b):
    # Convert lists to numpy arrays
    a = np.array(vec_a)
    b = np.array(vec_b)

    # Calculate the dot product
    dot_product = np.dot(a, b)

    # Check for orthogonality
    return dot_product == 0

vector1 = [1, 2, 3]
vector2 = [-2, 1, 0]

if are_orthogonal(vector1, vector2):
    print("The vectors are orthogonal.")
else:
    print("The vectors are not orthogonal.")
