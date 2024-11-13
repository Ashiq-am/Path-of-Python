import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(0)
data = pd.DataFrame({
    'variable_x': np.random.rand(100),
    'variable_y': np.random.rand(100),
    'category': np.random.choice(['A', 'B', 'C'], size=100)
})

sns.set_palette("husl")

sns.scatterplot(data=data, x='variable_x', y='variable_y', hue='category', style='category', size='category', palette='husl')

plt.title('GFG Plot with Seaborn Color Properties')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')

plt.legend(loc='upper right', title='Category')
plt.show()
