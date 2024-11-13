import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.DataFrame({
    'variable_x': np.random.rand(50),
    'variable_y': np.random.rand(50),
    'category': np.random.choice(['A', 'B', 'C'], size=50)
})

sns.scatterplot(data=data, x='variable_x', y='variable_y', hue='category')

plt.title('Geeks for Geeks Scatter Plot', color='green')
plt.xlabel('Variable X', color='green')
plt.ylabel('Variable Y', color='green')

plt.show()
