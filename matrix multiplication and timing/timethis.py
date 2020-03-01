# A timing decorated found in Python Cookbook by David Beaszley and Brian Jones (pp. 588)
# This decorated can be used to time selected functions

import time
from functools import wraps

# We define a wrapper that times the wrapped function.
def timethis(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		r = func(*args, **kwargs)
		end = time.perf_counter()
		print(f'{func.__module__}, {func.__name__}, {end - start}')
		return r
	return wrapper


@timethis # This line wraps the countdown(n) function and adds functionality to it.
def countdown(n):
	# This a simple counter.  We use it show how to use timethis.py and how it behave.
	while n>0:
		n -= 1

# We count down powers of 10 to show timethis in action.
# This takes about one minute to run.
for i in range(5):
	countdown(10 ** i)

"""
This is what the output looks like on my machine.
__main__, countdown, 1.0999999999969368e-06
__main__, countdown, 1.1999999999998123e-06
__main__, countdown, 5.299999999999749e-06
__main__, countdown, 4.5699999999995744e-05
__main__, countdown, 0.0004868000000000025
__main__, countdown, 0.003983800000000003
__main__, countdown, 0.0524969
__main__, countdown, 0.41072200000000003
__main__, countdown, 4.0116304000000005
__main__, countdown, 40.135166299999995
"""

from timeit import timeit

print('import math', timeit('math.sqrt(2)', 'import math'))
print('import math', timeit('sqrt(2)', 'from math import sqrt'))