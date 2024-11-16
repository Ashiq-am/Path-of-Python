import numpy as np

# Generate some example categorical data
categories = np.random.choice(['A', 'B', 'C', 'D'], size=100)

# Use numpy's unique function to get counts of each category
unique_categories, counts = np.unique(categories, return_counts=True)

# Print the result
print("Unique Categories:", unique_categories)
print("Category Counts:", counts)
