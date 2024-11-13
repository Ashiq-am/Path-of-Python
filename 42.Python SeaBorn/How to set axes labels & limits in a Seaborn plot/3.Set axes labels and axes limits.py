# import packages
import matplotlib.pyplot as plt
import seaborn as sns

# create data
data = [3, 7, 9, 11, 12, 14, 15, 16, 18, 19, 20, 23, 25, 28]

# plot distplot
fig, ax = plt.subplots()
sns.distplot(data, ax = ax)

# This will change the limits of the x-axis
ax.set_xlim(1, 70)

# This will add label to the X-axis
ax.set_xlabel( "GFG X")

# This will add label to the Y-axis
ax.set_ylabel( "GFG Y")

# This will add title to the plot
ax.set_title( "GFG - GFG")
plt.show()
