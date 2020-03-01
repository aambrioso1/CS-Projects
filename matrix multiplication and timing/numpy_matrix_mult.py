"""
We introduce the numpy matmul operation.
We show how the timeit.timeit function can be used to time a small fragment of code.
We also show how cProfile can be used to profile a function.
"""

import numpy as np

print('The matmul operation')
print('*' * 20)
A = np.array([[1, 0], [0, 1]])
B = np.array([[4, 1], [2, 2]])
print(f'A = {A}, B = {B}')
print('AB =', np.matmul(A, B))

print('The matmul operation with large matrices')
print('*' * 20)
for i in range(1,3):
	n = 10 ** i
	C = np.random.randn(n,n)
	D = np.random.randn(n,n)
	print(f'CD[{i}] =', np.matmul(C, D))

print(f'C = {C}, D = {D}')

# Here we show how the timeit.timeit function can be used to time a small code fragment
from timeit import timeit

NUM = 100
SIZE = 1000

func_string = f'matmul(random.randn({SIZE},{SIZE}),random.randn({SIZE},{SIZE}))'

Total_Time = timeit(func_string, 'from numpy import matmul, random', number = NUM)

print('Using timeit.timeit on matmul operation with large matrices')
print(f'The total time for a {SIZE}x{SIZE} matrix using numpy.matmul and a number of trials of {NUM} is {Total_Time} seconds')
print('*' * 20)

# Here is an example of profiling a function with cProfile
import cProfile
print('cProfile results')
cProfile.run('np.matmul(np.random.randn(100,100), np.random.randn(100,100))')