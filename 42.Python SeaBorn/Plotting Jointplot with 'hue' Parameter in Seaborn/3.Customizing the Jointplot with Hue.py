import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
iris = sns.load_dataset("iris")

# Create a JointGrid
g = sns.JointGrid(data=iris, x="sepal_length", y="sepal_width", hue="species")

# Add the scatterplot to the JointGrid
g = g.plot(sns.scatterplot, sns.kdeplot)

# Display the plot
plt.show()
