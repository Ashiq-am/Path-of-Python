import matplotlib.pyplot as plt


# initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

# Creating the figure and subplots
# according the argument passed
fig, axes = plt.subplots(1, 2)

# plotting the data in the
# 1st subplot
axes[0].plot(x, y)

# plotting the data in the 1st
# subplot only
axes[0].plot(y, x)

# plotting the data in the 2nd
# subplot only
axes[1].plot(x, y)
