import numpy as np

A = np.array([[2,4,6],
              [1,3,5]])
B = np.array([[1,1,1],
              [2,2,2]])
print("A + B =\n", A + B)
print("A - B =\n", A - B)
print("A x B.T =\n",np.dot(A, B.T))