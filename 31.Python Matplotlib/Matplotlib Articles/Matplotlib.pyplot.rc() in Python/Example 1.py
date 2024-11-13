from cycler import cycler
import numpy as np
import matplotlib.pyplot as plt


# setting up a custom cycler
sample_cycler = (cycler(color =['r', 'g',
								'b', 'y']) +
				cycler(lw =[1, 2, 3, 4]))

# using the rc function
plt.rc('lines', linewidth = 4)
plt.rc('axes', prop_cycle = sample_cycler)

A = np.linspace(0, 2 * np.pi, 50)
line_offsets = np.linspace(0, 2 * np.pi, 4,
						endpoint = False)

B = np.transpose([np.sin(A + phi) for phi in line_offsets])

figure, (axes0, axes1) = plt.subplots(nrows = 2)
axes0.plot(B)
axes0.set_title('Set default color cycle to 1st plot')

axes1.set_prop_cycle(sample_cycler)
axes1.plot(B)
axes1.set_title('Set axes color cycle to 2nd plot')

# Adding space between the two plots.
figure.subplots_adjust(hspace = 0.4)
plt.show()
