import numpy as np

# Transpose
A = np.array([[1, 2], [3, 4], [5, 6]])
print(f"Data = \n{A}\n\nTranspose Data = \n{A.T}\n\n")

# Matmul
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"Data:\nA =\n{A}\n\nB =\n{B}\n\nA x B =\n{np.matmul(A, B)}\n\n")

# Identity
A = np.array([[1, 2], [3, 4]])
I = np.eye(2, dtype=int)
print(f"A = \n{A}\n\nA x I = \n{A@I}")


