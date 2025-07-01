import numpy as np

# Determinant of a 3x3 matrix manually
def determinant_3x3(mat):
  a,b,c = mat[0]
  d,e,f = mat[1]
  g,h,i = mat[2]
  return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

mat13 = np.array([[2, -3, 1], [2, 0, -1], [1, 4, 5]])
print("Det = ", determinant_3x3(mat13), "\n\n")

# Invert a matrix if possible
def invert_matrix(mat):
  return np.linalg.inv(mat)

mat15 = np.array([[4, 7], [2, 6]])
inv15 = invert_matrix(mat15)
print("Inverse = \n", inv15, "\n\n")

# Class
class Matrix:
  def __init__(self, data):
    self.data = np.array(data, dtype=float)
    
  def add(self, other):
    return Matrix(self.data + other.data)
    
  def multiply(self, other):
    return Matrix(np.dot(self.data, other.data))
    
  def transpose(self):
    return Matrix(self.data.T)
    
  def inverse(self):
    return Matrix(np.linalg.inv(self.data))
    
  def __str__(self):
    return str(self.data)

matA = Matrix([[1, 2], [3, 4]])
matB = Matrix([[2, 0], [1, 2]])

print("Add:\n", matA.add(matB))
print("Multiply:\n", matA.multiply(matB))
print("Transpose:\n", matA.transpose())
print("Inverse:\n", matA.inverse())
print("Hello World")