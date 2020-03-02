"""
Matrix Multiplication
So far the script only creates an n x n matrix of random numbers.

"""

# We create a n x n matrix of random numbers.
import random as rd

n = 5
matrix = [[rd.random() for i in range(n)] for i in range(n)]
print('matrix = ', matrix)
print('element =', matrix[0][4])

def my_matmul(X, Y):
	result = [[sum(a*b for a,b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
	print('result', result)
	return result

print('my_matmul')
print('*' * 20)
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(f'A = {A}, B = {B}')
print('AB =', my_matmul(A, B))
