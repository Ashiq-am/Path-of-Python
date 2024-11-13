# import packages
import matplotlib.pyplot as plt
import seaborn as sns

# create data
data = [3, 7, 9, 11, 12, 14, 15, 16, 18, 19, 20, 23, 25, 28]

# plot distplot
fig, ax = plt.subplots()
sns.distplot(data, ax = ax)

# change the limits of X-axis
ax.set_xlim(1, 70)
plt.show()
