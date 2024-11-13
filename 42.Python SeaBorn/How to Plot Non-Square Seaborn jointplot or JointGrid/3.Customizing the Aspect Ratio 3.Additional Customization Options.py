import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.random.randn(1000)
y = 0.2 * np.random.randn(1000) + 0.5
df = pd.DataFrame(dict(x=x, y=y))

# Create the JointGrid with a custom ratio
g = sns.JointGrid(data=df, x="x", y="y", ratio=2)

# Plot the joint and marginal distributions
g.plot(sns.scatterplot, sns.histplot)
g.fig.set_figwidth(7.50)
g.fig.set_figheight(3.50)

plt.show()
