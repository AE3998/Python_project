"""
https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py

"""
import matplotlib.pyplot as plt
import numpy as np

"""
# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

print(t, "\n", s)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set( xlabel='time (s)',
        ylabel='voltage (mV)',
        title='About as simple as it gets, folks')
ax.grid()

# fig.savefig("test.png")
plt.show()
"""
# Otro test, mas basico
"""
https://matplotlib.org/stable/plot_types/basic/plot.html
"""

# Para verificar cuales son los style, puedo usar 
# print(plt.style.available)

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 100)
y = 4 + 2*np.sin(2*x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth = 1)
ax.set(
    xlim = (0, 8), 
    ylim = (0, 8),

    title = "Primer plot",
    xlabel = "x",
    ylabel = "4 + 2*np.sin(2*x)",
    
    # xticks = np.arange(1, 12),
    # yticks = np.arange(1, 8)
)

ax.grid(True)
plt.show()
