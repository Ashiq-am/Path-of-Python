import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generating random data
np.random.seed(42)
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(5, 1, 100)

# Creating a figure with 2 subplots
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Plotting Boxplot
sns.boxplot(data=[data1, data2], ax=ax[0])
ax[0].set_title("Box Plot")

# Plotting Violinplot
sns.violinplot(data=[data1, data2], ax=ax[1])
ax[1].set_title("Violin Plot")

# Displaying the plots
plt.tight_layout()
plt.show()
