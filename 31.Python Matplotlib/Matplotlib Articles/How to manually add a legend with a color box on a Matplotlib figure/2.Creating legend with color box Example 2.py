# Import libraries
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import scipy.stats
import numpy as np

# Setting limit for x values
x_min = 0.0
x_max = 50.0

# Setting figure size
fig = plt.figure(figsize = (16, 9))

# Creating first dataset
mean = 12.0
std = 3.0

x = np.linspace(x_min, x_max, 100)
y = scipy.stats.norm.pdf(x,mean,std)

# Plotting first dataset
plt.plot(x,y, color='red')
plt.fill_between(x, y, color='#CE5D45', alpha=1.0)

# Creating second dataset
mean = 18.0
std = 6.0

x = np.linspace(x_min, x_max, 100)
y = scipy.stats.norm.pdf(x,mean,std)

# Plotting second dataset
plt.plot(x,y, color='green')
plt.fill_between(x, y, color='#5DC83F', alpha=1.0)

# Creating legend with color box
pop_a = mpatches.Patch(color='#5DC83F', label='Population Dataset 1')
pop_b = mpatches.Patch(color='#CE5D45', label='Population Dataset 2')
plt.legend(handles=[pop_a,pop_b])

# Adding grid to plot
plt.grid()

# Adding X and Y limits
plt.xlim(x_min,x_max)
plt.ylim(0,0.25)

# Adding title
plt.title('simple legend example',fontsize=12)

# Adding labels
plt.xlabel('')
plt.ylabel('Probability Distribution')

# Showing plot
plt.show()
