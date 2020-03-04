# We implement the Strassen methood for  of mathrix co
# https://en.wikipedia.org/wiki/Strassen_algorithm

import random as rd

n = 2

"""
A = [[rd.random() for i in range(n)] for j in range(n)]
B = [[rd.random() for i in range(n)] for j in range(n)]

A = [[1 for i in range(n)] for j in range(n)]
B = [[1 for i in range(n)] for j in range(n)]
"""

A = [[1,2], [3,4]]
B = [[5,6], [7,8]]

def add(A,B):
	return [[A[i][j] + B[i][j] for i in range(n)] for j in range(n)]


def subtract(A,B):
	return [[A[i][j] - B[i][j] for i in range(n)] for j in range(n)]

# Just does base case when multiplying two 2 x 2 matrices.
def strassen_mul(A,B):
	if len(A) == 2:
		M1 = (A[0][0] + A[1][1])*(B[0][0] + B[1][1])
		M2 = (A[1][0] + A[1][1])*B[0][0]
		M3 = A[0][0]*(B[0][1] - B[1][1])
		M4 = A[1][1]*(B[1][0] - B[0][0])
		M5 = (A[0][0] + A[0][1])*B[1][1]
		M6 = (A[1][0] - A[0][0])*(B[0][0] + B[0][1])
		M7 = (A[0][1] - A[1][1])*(B[1][0] + B[1][1])
		C11 = M1 + M4 - M5 + M7
		C12 = M3 + M5
		C21 = M2 + M4
		C22 = M1 - M2 + M3 + M6
		return [[C11, C12], [C21, C22]]
	return print("Wrong size")



print(f'length of A = {len(A)}, A + B = {add(A,B)}')
print(f'A - B = {subtract(A,B)}, AB = {strassen_mul(A,B)}')
