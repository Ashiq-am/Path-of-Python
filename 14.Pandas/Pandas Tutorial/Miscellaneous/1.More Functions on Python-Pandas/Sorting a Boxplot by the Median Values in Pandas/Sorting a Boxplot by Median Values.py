import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Sample DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'] * 5, # Changed from * 10 to * 5 to match the length of 'Values'
    'Values': [10, 20, 15, 30, 25, 11, 18, 13, 35, 22, 9, 21, 14, 31, 23,
               12, 19, 16, 28, 24, 8, 17, 14, 29, 26]
}
df = pd.DataFrame(data)

# Compute the median for each category and sort by the median
category_median = df.groupby('Category')['Values'].median().reset_index()
category_median_sorted = category_median.sort_values(by='Values')

# Reorder the categories in the DataFrame based on the sorted median
df['Category'] = pd.Categorical(df['Category'],
                                categories=category_median_sorted['Category'],
                                ordered=True)

# Create the boxplot sorted by median
plt.figure(figsize=(8, 6))
sns.boxplot(x='Category', y='Values', data=df)
plt.title('Boxplot Sorted by Median Values')
plt.show()
