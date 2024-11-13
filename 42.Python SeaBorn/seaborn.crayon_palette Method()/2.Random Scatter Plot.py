import numpy as np
import seaborn as sns

np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.randint(0, 5, 100)

palette = sns.crayon_palette(['Red', 'Green', 'Black', 'Sunglow', 'Vivid Violet'])

sns.scatterplot(x=x, y=y, hue=colors, palette=palette)
plt.legend(title='Colors', loc='upper right')
plt.show()
