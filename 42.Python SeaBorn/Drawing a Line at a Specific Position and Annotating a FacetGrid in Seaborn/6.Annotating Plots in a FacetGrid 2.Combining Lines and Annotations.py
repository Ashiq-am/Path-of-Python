import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
tips = sns.load_dataset("tips")

# Create the FacetGrid
g = sns.FacetGrid(tips, col="smoker", height=7, aspect=0.6)
g.map(sns.boxplot, "sex", "total_bill", palette='viridis', order=['Male', 'Female'])

# Add horizontal lines and annotations
axes = g.axes.flatten()
axes[0].axhline(y=10, color='r', linestyle='--')
axes[1].axhline(y=30, color='b', linestyle='--')
axes[0].text(0.5, 10, 'Line at 10', ha='center', va='center', fontsize=12, color='red')
axes[1].text(1.5, 30, 'Line at 30', ha='center', va='center', fontsize=12, color='blue')

# Show the plot
plt.show()
