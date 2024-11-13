import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50],
    'category': ['A', 'B', 'A', 'B', 'A'],
    'size': [100, 150, 200, 250, 300]
}

# Creating a scatterplot with marker size based on a column
sns.scatterplot(x='x', y='y', hue='category', data=data)
plt.scatter(data['x'], data['y'], s=data['size'], marker='o')

plt.title('Scatterplot with Marker Size')
plt.show()
