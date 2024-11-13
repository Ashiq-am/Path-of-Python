import matplotlib.pyplot as plt


plt.subplot(332)
plt.plot([1, 2, 3, 4])

# setting the axes attributes
# before the call to subplot
plt.rc('font', weight ='bold')
plt.rc('xtick.major', size = 5, pad = 7)
plt.rc('xtick', labelsize = 15)

# setting aliases for color, linestyle
# and linewidth; gray, solid, thick
plt.rc('grid', c ='0.3', ls ='-', lw = 4)
plt.rc('lines', lw = 2, color ='g')
plt.subplot(312)

plt.plot([1, 2, 3, 4])
plt.grid(True)

# set changes to default value
plt.rcdefaults()
plt.subplot(313)
plt.plot([1, 2, 3, 4])
plt.grid(True)
plt.show()
