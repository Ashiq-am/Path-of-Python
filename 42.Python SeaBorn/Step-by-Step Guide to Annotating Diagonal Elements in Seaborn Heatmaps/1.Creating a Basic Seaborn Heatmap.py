import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.random.rand(5, 5)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])
# Plot the heatmap
sns.heatmap(df, annot=True, cmap='viridis')
plt.show()
