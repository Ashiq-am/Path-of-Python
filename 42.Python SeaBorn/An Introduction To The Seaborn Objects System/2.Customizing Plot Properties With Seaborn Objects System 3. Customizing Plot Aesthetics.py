import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")

# Set the style
sns.set_style("whitegrid")

# Create a customized scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="smoker", style="time", size="size", palette="coolwarm", markers=["o", "s"])
plt.title("Customized Scatter Plot")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()
