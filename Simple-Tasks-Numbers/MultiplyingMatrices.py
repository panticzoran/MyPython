# Multiplying matrices

import numpy as np

a = np.array([[1, 2, 5], [3, 4, 6], [3, 4, 6]])
b = np.array([[5, 6, 8], [7, 8, 9], [3, 4, 6]])

print("Matrix A: \n", a)
print("\n")
print("Matrix B: \n", b)
print("\n")

c = np.matmul(a, b)
print("Matrix A x B:")
print(c)

print("\n")