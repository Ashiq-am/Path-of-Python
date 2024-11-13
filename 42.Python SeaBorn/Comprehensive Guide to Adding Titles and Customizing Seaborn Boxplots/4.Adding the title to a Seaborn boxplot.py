import seaborn as sns
import matplotlib.pyplot as plt

# Load the "tips" dataset
tips = sns.load_dataset("tips")

# Create the boxplot
sns.boxplot(x="day", y="total_bill", data=tips)

# Add title to the boxplot
plt.title("Total Bill Distribution by Day")

# Add labels
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill")

# Display the boxplot
plt.show()
