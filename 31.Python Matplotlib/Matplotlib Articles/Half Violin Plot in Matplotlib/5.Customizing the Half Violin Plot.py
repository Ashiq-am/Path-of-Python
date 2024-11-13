import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
data = np.random.normal(loc=0, scale=1, size=100)

# Create the violin plot
fig, ax = plt.subplots()
parts = ax.violinplot(data, showmeans=False, showmedians=True)

# Customize the violin plot appearance
for pc in parts['bodies']:
    pc.set_facecolor('skyblue')  # Set the fill color
    pc.set_edgecolor('black')    # Set the edge color
    pc.set_alpha(0.8)            # Set the transparency level

plt.title("Customized Violin Plot")
plt.show()
