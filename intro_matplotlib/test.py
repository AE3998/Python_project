import matplotlib.pyplot as plt
import numpy as np

# xdata = np.linspace(0, 2, 20)
# data1 = np.sin(xdata*2*np.pi)

data1 = np.random.randn(20)
xdata = np.arange(len(data1))

# fig, ax = plt.subplots()
# ax.plot(xdata, data1)
# ax.set(
#     xlabel = "xdata",
#     ylabel = "data 1",
#     title = "titulo",
#     # xticks = (np.arange(0, 100, 30), ['zero', '30', 'sixty', '90']),
#     xticks = np.arange(0, 100, 30)
# )

plt.show()

fig, axs = plt.subplots(1, 2, layout = 'constrained')
axs[0].plot(xdata, data1)
axs[0].set_title('Automatic ticks')

axs[1].plot(xdata, data1)
axs[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])
axs[1].set_yticks([-1.5, 0, 1.5])  # note that we don't need to specify labels
axs[1].set_title('Manual ticks')
axs[1].grid(True)
plt.show()