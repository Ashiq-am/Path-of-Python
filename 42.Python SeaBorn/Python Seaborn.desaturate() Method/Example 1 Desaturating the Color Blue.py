import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

# Display first few rows of the dataset
iris.head()

# Desaturate the color blue with a saturation level of 0.5
desaturated_blue = sns.desaturate("blue", 0.5)

# Plot the desaturated color
sns.palplot(desaturated_blue)
plt.show()
