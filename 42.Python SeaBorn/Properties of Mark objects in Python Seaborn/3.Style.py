import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(0)
data = pd.DataFrame({
    'variable_x': np.random.rand(50),
    'variable_y': np.random.rand(50),
    'category': np.random.choice(['A', 'B', 'C'], size=50)
})


sns.scatterplot(data=data, x='variable_x', y='variable_y', hue='category', style='category', s=100)

plt.title('GFG Scatter Plot')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')

plt.legend(title='Category', loc='upper right')
plt.show()
