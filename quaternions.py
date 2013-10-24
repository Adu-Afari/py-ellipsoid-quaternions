#!/usr/bin/env python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")

# Set of all spherical angles:
res = 16
u = np.linspace(0, 2 * np.pi, 2*res+1)
v = np.linspace(0, np.pi, res+1)

# Cartesian coordinates that correspond to the spherical angles:
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones_like(u), np.cos(v))

ax.plot_wireframe(x, y, z)

xyz = np.transpose([x, y, z])
T = 

plt.show()
