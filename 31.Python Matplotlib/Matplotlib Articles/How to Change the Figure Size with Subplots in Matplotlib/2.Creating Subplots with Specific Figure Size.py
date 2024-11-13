import matplotlib.pyplot as plt

# Create a 2x2 grid of subplots with a specific figure size
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].plot([1, 2, 3, 4], [1, 4, 9, 16])
axs[0, 1].plot([1, 2, 3, 4], [1, 2, 3, 4])
axs[1, 0].plot([1, 2, 3, 4], [1, 3, 6, 10])
axs[1, 1].plot([1, 2, 3, 4], [10, 9, 8, 7])
plt.show()
