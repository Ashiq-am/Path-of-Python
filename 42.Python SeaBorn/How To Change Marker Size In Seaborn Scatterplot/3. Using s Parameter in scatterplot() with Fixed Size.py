import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 15, 12, 17, 20]
}

# Create a scatterplot with fixed marker size
sns.scatterplot(x='x', y='y', s=200, data=data)
plt.show()
