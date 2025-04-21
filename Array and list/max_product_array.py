import numpy as np

arr = np.array([2, 42, 4, 21, 1])

def max_product(arr):
    arr = sorted(arr)  # Convert to list and sort
    return arr[-1] * arr[-2]  # Multiply two largest numbers

print("Maximum product is:", max_product(arr))
