# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

# Prepare arrays x, y, z

"""
Using np.linspace
Documentation for linspace
https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
"""
"""
# Using np.linspace
x = np.arange(0, 10, 0.2)
y = 2*x + 1
z = y


# Using lists
x = [t for t in range(100)]
y = [2*t for t in range(100)]
z = [3*t ** 2 for t in range(100)]

"""
# Parametric spiral found in Thomas Calculus 14th Edition, p. 770.
t = np.linspace(0, 10 * np.pi, 100)
x = t * np.cos(t)
y = t * np.sin(t)
z = t


ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()