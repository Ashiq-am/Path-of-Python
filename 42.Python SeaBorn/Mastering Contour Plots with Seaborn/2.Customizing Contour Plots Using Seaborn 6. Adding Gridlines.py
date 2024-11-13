import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.figure(figsize=(6, 6))

# Creating the contour plot
contour = sns.kdeplot(x=x, y=y, fill=True, cmap="coolwarm", thresh=0, levels=100)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
