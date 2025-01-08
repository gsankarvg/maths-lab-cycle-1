import numpy as np

def are_orthogonal(vec_a, vec_b):
    # Convert lists to numpy arrays
    a = np.array(vec_a)
    b = np.array(vec_b)

    # Calculate the dot product
    dot_product = np.dot(a, b)

    # Check for orthogonality
    return dot_product == 0

# Input for the first vector
vector1 = list(map(int, input("Enter the first vector (space-separated): ").split()))

# Input for the second vector
vector2 = list(map(int, input("Enter the second vector (space-separated): ").split()))

# Display the input vectors
print(f"Vector 1: {vector1}")
print(f"Vector 2: {vector2}")

if are_orthogonal(vector1, vector2):
    print("The vectors are orthogonal.")
else:
    print("The vectors are not orthogonal.")
