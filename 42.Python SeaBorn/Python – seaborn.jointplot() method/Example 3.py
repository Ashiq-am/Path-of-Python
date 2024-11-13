# importing required packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("exercise")

# draw jointplot with
# kde kind
sns.jointplot(x = "id", y = "pulse",
			kind = "kde", data = data)
# Show the plot
plt.show()


