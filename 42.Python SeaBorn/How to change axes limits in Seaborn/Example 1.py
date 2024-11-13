# Import module
import matplotlib.pyplot as plt
import seaborn as sns

# assing data
data = [3, 7, 9, 11, 12, 14,
		15, 16, 18, 19, 20,
		23, 25, 28]

# depict visualization
fig, ax = plt.subplots()
sns.distplot(data, ax=ax)
ax.set_xlim(1, 70)
plt.show()
