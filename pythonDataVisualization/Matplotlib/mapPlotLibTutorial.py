import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

# ------------------------------------------------------------ #
# OBJECT ORIENTED METHOD of data visualization with matplotlib #
# ------------------------------------------------------------ #

# Creates blank canvas
fig1 = plt.figure()

axes1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes | left, bottom, width, height (range 0 to 1)
axes2 = fig1.add_axes([0.2, 0.5, 0.4, 0.3]) # inset axes | left, bottom, width, height (range 0 to 1)

# Larger Figure Axes 1
axes1.plot(x, y, 'b')
axes1.set_xlabel('X_label_axes2')
axes1.set_ylabel('Y_label_axes2')
axes1.set_title('Axes 1 Title')

# Insert Figure Axes 2
axes2.plot(y, x, 'r')
axes2.set_xlabel('X_label_axes2')
axes2.set_ylabel('Y_label_axes2')
axes2.set_title('Axes 2 Title')
plt.show()

# ------------------------------------------------------------ #
# subplots()
# ------------------------------------------------------------ #

# A common issue with matplolib is overlapping subplots or figures. We ca use fig.tight_layout() or plt.tight_layout()
# method, which automatically adjusts the positions of the axes on the figure canvas so that there is no overlapping
# content
# Empty canvas of 1 by 2 subplots
fig2, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x, y, 'g')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('subplots example')

plt.tight_layout()
plt.show()

# ------------------------------------------------------------ #
# Figure size, aspect ratio and DPI
# ------------------------------------------------------------ #

# Matplotlib allows the aspect ratio, DPI and figure size to be specified when the Figure object is created.
# You can use the figsize and  dpi keyword arguments.

#   figsize is a tuple of the width and height of the figure in inches
#   dpi is the dots-per-inch (pixel per inch).
fig3, axes3 = plt.subplots(figsize=(12, 3))

axes3.plot(x, y, 'r')
axes3.set_xlabel('x')
axes3.set_ylabel('y')
axes3.set_title('Figure size, aspect ratio and DPI')
plt.show()


# ------------------------------------------------------------ #
# Legends, labels and titles
# ------------------------------------------------------------ #
fig4 = plt.figure()

ax4 = fig4.add_axes([0, 0, 1, 1])
ax4.plot(x, x**2, label="x**2")
ax4.plot(x, x**3, label="x**3")
ax4.legend()


# Lots of options....# Lots o

ax4.legend(loc=1) # upper right corner
ax4.legend(loc=2) # upper left corner
ax4.legend(loc=3) # lower left corner
ax4.legend(loc=4) # lower right corner

# .. many more options are available

# Most common to choose
ax4.legend(loc=0) # let matplotlib decide the optimal location
ax4.set_title("Legends, labels and titles")
plt.show()


# ------------------------------------------------------------ #
# Setting colors, linewidths, linetypes
# ------------------------------------------------------------ #

fig5, ax5 = plt.subplots(figsize=(12, 6))

ax5.plot(x, x+1, color="red", linewidth=0.25)
ax5.plot(x, x+2, color="red", linewidth=0.50)
ax5.plot(x, x+3, color="red", linewidth=1.00)
ax5.plot(x, x+4, color="red", linewidth=2.00)

# possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax5.plot(x, x+5, color="green", lw=3, linestyle='-')
ax5.plot(x, x+6, color="green", lw=3, ls='-.')
ax5.plot(x, x+7, color="green", lw=3, ls=':')

# custom dash
line5, = ax5.plot(x, x+8, color="black", lw=1.50)
line5.set_dashes([5, 10, 15, 10]) # format: line length, space length, ...

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax5.plot(x, x+ 9, color="blue", lw=3, ls='-', marker='+')
ax5.plot(x, x+10, color="blue", lw=3, ls='--', marker='o')
ax5.plot(x, x+11, color="blue", lw=3, ls='-', marker='s')
ax5.plot(x, x+12, color="blue", lw=3, ls='--', marker='1')

# marker size and color
ax5.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax5.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax5.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax5.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8,
        markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green")

plt.show()


# ------------------------------------------------------------ #
# Plot range
# ------------------------------------------------------------ #

# We can configure the ranges of the axes using the set_ylim and set_xlim methods in the axis object, or axis('tight')
# for automatically getting "tightly fitted" axes ranges

fig6, axes6 = plt.subplots(1, 3, figsize=(12, 4))

axes6[0].plot(x, x**2, x, x**3)
axes6[0].set_title("default axes ranges")

axes6[1].plot(x, x**2, x, x**3)
axes6[1].axis('tight')
axes6[1].set_title("tight axes")

axes6[2].plot(x, x**2, x, x**3)
axes6[2].set_ylim([0, 60])
axes6[2].set_xlim([2, 5])
axes6[2].set_title("custom axes range")
plt.show()


# ------------------------------------------------------------ #
# Special Plot Types
# ------------------------------------------------------------ #
plt.scatter(x, y)


plt.show()
from random import sample
data = sample(range(1, 1000), 100)
plt.hist(data)
plt.show()


data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data, vert=True, patch_artist=True)
plt.show()

