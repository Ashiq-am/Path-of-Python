import matplotlib.pyplot as plt

# Set default figure size and DPI globally
plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['figure.dpi'] = 150

# Now all figures will use these settings by default
plt.plot([1, 2, 3], [1, 4, 9])
plt.title('Global Default Settings Applied')
plt.show()