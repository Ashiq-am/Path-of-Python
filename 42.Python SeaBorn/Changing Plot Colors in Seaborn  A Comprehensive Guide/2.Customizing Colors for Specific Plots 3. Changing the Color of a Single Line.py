import seaborn as sns
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'sales': [3, 3, 5, 4, 5, 6, 8, 9, 14, 18]
})

# Create a line plot with a specific color
sns.lineplot(data=df, x='day', y='sales', color='red')
