# importing matplotlib module and respective classes
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator,
							FormatStrFormatter,
							AutoMinorLocator)

x = [3, 2, 7, 4, 9]
y = [10, 4, 7, 1, 2]

fig, ax = plt.subplots()

ax.set_title('Example Graph')

ax.set_ylabel('y-AXIS')
ax.set_xlabel('x-AXIS')

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Make x-axis with major ticks that
# are multiples of 11 and Label major
# ticks with '% 1.2f' formatting
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_major_formatter(FormatStrFormatter('% 1.2f'))

# make x-axis with minor ticks that
# are multiples of 1 and label minor
# ticks with '% 1.2f' formatting
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.xaxis.set_minor_formatter(FormatStrFormatter('% 1.2f'))

ax.plot(x, y)
plt.show()
