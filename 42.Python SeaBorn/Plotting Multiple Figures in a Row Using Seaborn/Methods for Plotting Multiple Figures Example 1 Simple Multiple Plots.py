import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the example dataset
iris = sns.load_dataset("iris")

# Create a figure with 1 row and 3 columns
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Plot on the first subplot
sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", ax=axes[0])
axes[0].set_title('Sepal Length vs Sepal Width')

# Plot on the second subplot
sns.scatterplot(data=iris, x="petal_length", y="petal_width", ax=axes[1])
axes[1].set_title('Petal Length vs Petal Width')

# Plot on the third subplot
sns.scatterplot(data=iris, x="sepal_length", y="petal_length", ax=axes[2])
axes[2].set_title('Sepal Length vs Petal Length')

# Adjust the spacing between plots
plt.tight_layout()

# Display the plot
plt.show()
