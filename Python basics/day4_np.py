import numpy as np

# Matrix Multiplication
arr1 = np.array([23, 16])
arr2 = np.array([11, 22])
print(np.matmul(arr1, arr2))
print("\n\n")

# np.select
arr1 = np.array(['low', 'mid', 'mid', 'high'])
cond = [arr1 == "low", arr1 == "mid"]
choice = [0, 1]
print(np.select(cond, choice, default=2))
print("\n\n")


# Random
arr1 = np.random.rand(3,3)
arr2 = np.random.randn(3,3)
print(arr1, arr2, sep = "\n\n")
