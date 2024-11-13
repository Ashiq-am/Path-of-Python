import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 15, 12, 17, 20],
    'size': [100, 200, 300, 400, 500]  # Marker size data
})

# Create a relational plot with marker size
sns.relplot(x='x', y='y', data=data, kind='scatter', size='size')
plt.show()
