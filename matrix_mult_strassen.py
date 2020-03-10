# We implement the Strassen methood for  of mathrix co
# https://en.wikipedia.org/wiki/Strassen_algorithm
"""
Strassen method for matrix multiplicaton a square matrix 2^n x 2^n matrix into 2^(n-1) square submatices
"""
import random as rd

# This functions prints out a matrix line by line so that it is easy to read.
def printMat(M):
    s = [[str(e) for e in row] for row in M]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

# Matrix multiplication using the standard algorithm and list comprehension.
def my_matmul(X, Y):
	result = [[sum(a*b for a,b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
	return result

"""
We define the functions we need for the Strassen algorithm base on the this 
Wikipedia article:  
"""

# Adds two matrices
def add(A,B):
	n = len(A)
	return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

# Subtracts two matrices
def subtract(A,B):
	n=len(A)
	return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


#A matrix chopping function.  Cuts a 2^n x 2^n matrix into four square submatrices.
def chop_mat(M):
	n = len(M)
	A00 = [[M[i][j] for j in range(n//2)] for i in range(n//2)]
	A01 = [[M[i][j] for j in range(n//2)] for i in range(n//2,n)] 
	A10 = [[M[i][j] for j in range(n//2,n)] for i in range(n//2)]
	A11 = [[M[i][j] for j in range(n//2,n)] for i in range(n//2,n)]
	if len(A11) == 1:
		return [A00, A10, A01, A11]
	else:
		return [A00, A10, A01, A11]


def strassen_mul(A,B):
    size = len(A)
    if size == 2:
        M1 = (A[0][0] + A[1][1])*(B[0][0] + B[1][1])
        M2 = (A[1][0] + A[1][1])*B[0][0]
        M3 = A[0][0]*(B[0][1] - B[1][1])
        M4 = A[1][1]*(B[1][0] - B[0][0])
        M5 = (A[0][0] + A[0][1])*B[1][1]
        M6 = (A[1][0] - A[0][0])*(B[0][0] + B[0][1])
        M7 = (A[0][1] - A[1][1])*(B[1][0] + B[1][1])
        C00 = M1 + M4 - M5 + M7
        C01 = M3 + M5
        C10 = M2 + M4
        C11 = M1 - M2 + M3 + M6
        return [[C00, C01], [C10, C11]]
    if size > 2:
        P1 = chop_mat(A)
        P2 = chop_mat(B)
        A00 = P1[0]
        A01 = P1[1]
        A10 = P1[2]
        A11 = P1[3]
        B00 = P2[0]
        B01 = P2[1]
        B10 = P2[2]
        B11 = P2[3]
        p1_1 = add(A00, A11)
        p1_2 = add(B00, B11)
        p2 = add(A10, A11)
        p3 = subtract(B01, B11)
        p4 = subtract(B10, B00)
        p5 = add(A00, A01)
        p6_1 = subtract(A10,A00)
        p6_2 = add(B00, B01)
        p7_1 = subtract(A01, A11)
        p7_2 = add(B10, B11)
        M1 = strassen_mul(p1_1, p1_2)
        M2 = strassen_mul(p2, B00)
        M3 = strassen_mul(A00, p3)
        M4 = strassen_mul(A11, p4)
        M5 = strassen_mul(p5, B11)
        M6 = strassen_mul(p6_1, p6_2)
        M7 = strassen_mul(p7_1, p7_2)
        C00 = subtract(add(add(M1, M4), M7), M5)
        C01 = add(M3, M5)
        C10 = add(M2, M4)
        C11 = subtract(add(add(M1,M3), M6), M2)
        C = [[0 for j in range(size)] for i in range(size)]
        new_size = size//2
        for i in range(new_size):
            for j in range(new_size):
                C[i][j] = C00[i][j]
                C[i][j + new_size] = C01[i][j]
                C[i + new_size][j] = C10[i][j]
                C[i + new_size][j + new_size] = C11[i][j]
        return C
    else:
        print("Error in strassen_mul for len(A)")

# We define a few matrices for testing purposes.
A = [[1,2], [3,4]]
B = [[5,6], [7,8]]

C = [[1,2,3,4], [1,1,1,1], [5,6,7,8], [1,1,1,1]]
D = [[1,2,3,4], [5,6,7,8], [1,1,1,1], [1,1,1,1]]

n = 4
E = [[rd.randint(0,1) for j in range(2 ** n)] for i in range(2 ** n)]
F = [[rd.randint(0,1) for j in range(2 ** n)] for i in range(2 ** n)]

M2 = strassen_mul(E, F)
M1 = my_matmul(E, F)

print('E matrix')
printMat(E)
print('*'*60)
print('F matrix')
printMat(F)
print('*'*60)
print('Result of standard algorithm')
printMat(M1)
print('*'*60)
print('result of Strassen')
printMat(M2)
print('*'*60)
