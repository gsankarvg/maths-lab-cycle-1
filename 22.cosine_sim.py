import numpy as np

def cosine_similarity(vec_a, vec_b):
    # Convert lists to numpy arrays
    a = np.array(vec_a)
    b = np.array(vec_b)

    # Calculate the dot product and the norms of the vectors
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    # Calculate cosine similarity
    if norm_a == 0 or norm_b == 0:
        return 0.0  # Avoid division by zero
    return dot_product / (norm_a * norm_b)


vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

similarity = cosine_similarity(vector1, vector2)
print(f"Cosine Similarity: {similarity}")
