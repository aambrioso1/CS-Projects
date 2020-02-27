# A timing decorated found in Python Cookbook by David Beaszley and Brian Jones (pp. 588)
# This decorated can be used to time selected functions

import time
from functools import wraps

def timethis(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		r = func(*args, **kwargs)
		end = time.perf_counter()
		print(f'{func.__module__}, {func.__name__}, {end - start}')
		return r
	return wrapper


@timethis
def countdown(n):
	# This a simple counter program to show how to use timethis.py and how it behave.
	while n>0:
		n -= 1

for i in range(10):
	countdown(10 ** i)
