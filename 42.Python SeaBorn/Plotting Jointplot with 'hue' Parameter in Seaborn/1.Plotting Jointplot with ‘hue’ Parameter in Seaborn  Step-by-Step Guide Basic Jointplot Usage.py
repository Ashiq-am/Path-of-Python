import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
iris = sns.load_dataset("iris")

# Create a basic jointplot
sns.jointplot(data=iris, x="sepal_length", y="sepal_width")

# Display the plot
plt.show()
