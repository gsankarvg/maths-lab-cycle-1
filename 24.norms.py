import numpy as np

def calculate_norms(vector):
    vec = np.array(vector)

    # L1 norm
    l1_norm = np.linalg.norm(vec, 1)

    # L2 norm
    l2_norm = np.linalg.norm(vec, 2)

    # Squared L2 norm
    l2_squared_norm = np.linalg.norm(vec, 2) ** 2

    # max norm
    max_l = np.linalg.norm(vec, np.inf)

    return l1_norm, l2_norm, l2_squared_norm, max_l


v1 = list(map(int,input("enter the vector, separated by space: ").split()))
l1, l2, l2_squared, max_l = calculate_norms(v1)
print(f"L1 Norm: {l1}")
print(f"L2 Norm: {l2}")
print(f"Squared L2 Norm: {l2_squared}")
print(f"max norm : {max_l}")

