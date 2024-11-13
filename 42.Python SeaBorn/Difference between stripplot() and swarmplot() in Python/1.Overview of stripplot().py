import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset("tips")

# Create a strip plot
sns.stripplot(x="day", y="total_bill", data=data, jitter=True)
plt.title("Strip Plot of Total Bill by Day")
plt.show()
