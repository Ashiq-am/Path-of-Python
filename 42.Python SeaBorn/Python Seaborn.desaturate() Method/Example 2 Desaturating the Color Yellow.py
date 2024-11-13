import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

# Display first few rows of the dataset
iris.head()

# Desaturate the color yellow with a saturation level of 0.5
desaturated_yellow = sns.desaturate("yellow", 0.5)

# Plot the desaturated color
sns.palplot(desaturated_yellow)
plt.show()
