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

# Create a Seaborn barplot with a single color
plt.figure(figsize=(8, 6))
sns.barplot(x='Category', y='Values', data=df, color='skyblue')
plt.title('Barplot with Single Color')
plt.show()
