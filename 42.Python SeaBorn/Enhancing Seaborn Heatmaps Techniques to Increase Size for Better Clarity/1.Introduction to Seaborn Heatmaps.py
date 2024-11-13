import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
data = np.random.rand(10, 12)
df = pd.DataFrame(data, columns=[f'Col{i}' for i in range(1, 13)])

# Create a heatmap
sns.heatmap(df)
plt.show()
