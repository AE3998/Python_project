import numpy as np
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery-nogrid')

x = np.linspace(-4, 4, 10)
y = np.linspace(-4, 4, 10)

X, Y = np.meshgrid(x, y)

U = X + Y
V = X - Y

# plot
fig, ax = plt.subplots()

ax.quiver(X, Y, U, V, color = "C0", angles = 'xy',
          scale_units = 'xy', scale = 5, width = .005)

ax.set(xlim = (-5, 5), ylim = (-5, 5))
plt.show()