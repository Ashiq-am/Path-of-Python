import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'B', 'C', 'C', 'C']}
df = pd.DataFrame(data)

# Calculate value counts
counts = df['Category'].value_counts()

# Plot value counts
counts.plot(kind='bar', color='skyblue')
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Value Counts of Categories')
plt.show()
