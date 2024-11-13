# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 15, 25],
    'Subcategory': ['W', 'X', 'Y', 'Z']
}
df = pd.DataFrame(data)

# Create a Seaborn barplot with hue (different colors for each bar)
plt.figure(figsize=(8, 6))
sns.barplot(x='Category', y='Values', hue='Subcategory', data=df)
plt.title('Barplot with Hue')
plt.show()
