import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {'Category': ['A', 'B', 'C', 'D'], 'Values': [4, 20, 1, 15]}
df = pd.DataFrame(data)

# Create a barplot
sns.barplot(x='Category', y='Values', data=df)
plt.show()
