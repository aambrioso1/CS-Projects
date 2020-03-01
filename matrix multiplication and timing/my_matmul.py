"""
Matrix Multiplication

"""

import random as rd

# We create a n x n matrix of random numbers.
n = 5
matrix = [[rd.random() for i in range(n)] for i in range(n)]
print('matrix = ', matrix, 'element =', matrix[0][4])