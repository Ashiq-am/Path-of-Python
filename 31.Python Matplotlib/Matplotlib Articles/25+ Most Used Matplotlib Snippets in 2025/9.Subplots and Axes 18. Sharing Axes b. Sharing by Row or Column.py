# Create a 2x2 grid of subplots sharing x-axis by column and y-axis by row
fig, axs = plt.subplots(nrows=2, ncols=2, sharex='col', sharey='row')

axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sine Function')

axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cosine Function')

axs[1, 0].plot(x, y1**2)
axs[1, 0].set_title('Sine Squared Function')

axs[1, 1].plot(x, y2**2)
axs[1, 1].set_title('Cosine Squared Function')

plt.tight_layout()
plt.show()