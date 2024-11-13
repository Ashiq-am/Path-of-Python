# Load the example dataset
iris = sns.load_dataset("iris")

# Create a pairplot
sns.pairplot(iris, hue="species")

# Display the plot
plt.show()
