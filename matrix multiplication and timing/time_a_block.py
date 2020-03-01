"""
The shows how to use a context manager to time a block of code.
The code idea comes from Beazley and Jones's Python Cookbook (pp. 588-599)
"""
import time
from contextlib import contextmanager
import numpy as np


# We create a context manager to time a block of code.
@contextmanager
def timeblock(label):
	start = time.perf_counter()
	try:
		yield
	finally:
		end = time.perf_counter()
		print(f'{label} : {end - start}')

# Code for timing a a block of 
with timeblock('Time of the block'):
	# The for loop is the block of code that is timed.
	# We multiply two matrices of increasing size.
	
	NUM = 3 # Highest power of 10 used in the loop
	
	for i in range(1,NUM+1):
		n = 10 ** i # The size of the matrices
		C = np.random.randn(n,n)
		D = np.random.randn(n,n)
		print(f'Multiplying two {n}x{n} =', np.matmul(C, D))
