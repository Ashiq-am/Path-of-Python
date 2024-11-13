import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


fig, ax = plt.subplots()
ax.axis([0.01, 10000, 1, 1000000])
ax.loglog()

for axis in [ax.xaxis, ax.yaxis]:
	formatter = FuncFormatter(lambda y, _: '{:.16g}'.format(y))
	axis.set_major_formatter(formatter)

plt.show()
