import matplotlib.pyplot as plt

# Creating the figure and subplots
# according the argument passed
fig, axes = plt.subplots(1, 2)

# plotting the data in the 1st subplot
axes[0].plot([1, 2, 3, 4], [1, 2, 3, 4])

# plotting the data in the 1st subplot only
axes[0].plot([1, 2, 3, 4], [4, 3, 2, 1])

# plotting the data in the 2nd subplot only
axes[1].plot([1, 2, 3, 4], [1, 1, 1, 1])
