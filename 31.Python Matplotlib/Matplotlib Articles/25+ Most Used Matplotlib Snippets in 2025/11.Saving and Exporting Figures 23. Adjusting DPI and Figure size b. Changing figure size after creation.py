fig = plt.figure()
plt.plot([1, 2, 3], [1, 4, 9])

# Change figure size and DPI
fig.set_size_inches(10, 5)     # Set new size
fig.set_dpi(150)               # Set new DPI
plt.title('Updated Figure Size and DPI')
plt.show()