import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 15, 12, 17, 20],
    'size': [100, 200, 300, 400, 500]  # Marker size data
}

# Create a scatterplot with marker size
sns.scatterplot(x='x', y='y', size='size', data=data)

# Show the plot
plt.show()
