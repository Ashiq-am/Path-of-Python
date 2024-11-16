import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'B', 'C', 'C', 'C']}
df = pd.DataFrame(data)

# Calculate value counts
counts = df['Category'].value_counts()

# Plot value counts as pie chart
counts.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Distribution of Categories')
plt.ylabel('')
plt.show()
