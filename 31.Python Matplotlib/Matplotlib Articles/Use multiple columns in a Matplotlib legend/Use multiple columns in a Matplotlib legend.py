# code
import matplotlib.pyplot as plt

plt.plot([0, 3], [0, 2.0], label='Label 1')
plt.plot([0, 3], [0, 2.1], label='Label 2')
plt.plot([0, 3], [0, 2.2], label='Label 3')
plt.plot([0, 3], [0, 2.3], label='Label 4')
plt.plot([0, 3], [0, 2.4], label='Label 5')

# Change the number of columns here
plt.legend(ncol=3)

plt.show()
