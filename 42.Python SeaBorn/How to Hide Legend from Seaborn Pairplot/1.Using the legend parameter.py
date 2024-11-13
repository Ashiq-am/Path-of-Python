import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'id': ['1', '2', '1', '2', '2', '6', '7', '7', '6', '6'],
    'x': [123, 22, 356, 412, 54, 634, 72, 812, 129, 110],
    'y': [120, 12, 35, 41, 45, 63, 17, 91, 112, 151]
})

# Create pairplot without legend
sns.pairplot(df, x_vars='x', y_vars='y', hue='id', height=3, plot_kws={'legend': False})
plt.show()
