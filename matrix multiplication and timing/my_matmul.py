"""
Matrix Multiplication Profiling

"""

# import cProfile
# import timethis.py

import random as rd
import time
from functools import wraps
import matplotlib.pyplot as plt

def plot(x_list, y_list):
	# This function simply plots the values in the x_list against those in the y_list
    plt.plot(x_list, y_list)
    plt.show()

# This is a wrapper that times the wrapped function.
def timethis(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		r = func(*args, **kwargs)
		end = time.perf_counter()
		"""
		Note the change here so the wrapper will return the time that the wrap function takes.
		"""
		# print(f'{func.__module__}, {func.__name__}, {end - start}')
		return end - start
	return wrapper


"""
A = [[1,2], [3,4]]
B = [[5,6], [7,8]]

C = [[1,2,3,4], [1,1,1,1], [5,6,7,8], [1,1,1,1]]
D = [[1,2,3,4], [5,6,7,8], [1,1,1,1], [1,1,1,1]]

def my_matmul(X, Y):
	result = [[sum(a*b for a,b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
	return result

print(my_matmul(A,B))
print(my_matmul(C,D))
"""

@timethis
def my_matmul_timed(X, Y):
	result = [[sum(a*b for a,b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
	return result

start = 2
end = 100
x_s = [i for i in range(start, end)]
y_s = []
for size in range(start,end):
	# size = 2 ** exp
	E = [[rd.randint(-10,10) for i in range(size)] for j in range(size)]
	F = [[rd.randint(-10,10) for i in range(size)] for j in range(size)]
	y_s.append(my_matmul_timed(E,F))

plot(x_s, y_s)


"""
To use this profiler use must pip install memory-profiler with the commmand:   pip install memory-profiler
Once installed use the function wrapper @profile to get a report
"""
"""
@profile
def my_matmul_mem(X, Y):
	result = [[sum(a*b for a,b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
	return result

for n in range(10,51,10):
	A = [[rd.random() for i in range(n)] for i in range(n)]
	B = [[rd.random() for i in range(n)] for i in range(n)]
	print(f'n = {n}')
	my_matmul_timed(A, B)
	my_matmul_mem(A,B)



"""
"""
print('cProfile results')
cProfile.run('2 ** 1000')
"""