# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 15, 25]
}
df = pd.DataFrame(data)

# Create a Seaborn barplot with a color palette
plt.figure(figsize=(8, 6))
sns.barplot(x='Category', y='Values', data=df, palette='Set2')
plt.title('Barplot with Color Palette')
plt.show()
