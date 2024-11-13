import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create example data
np.random.seed(42)
categories = ['Category A', 'Category B', 'Category C']
data = {
    'Category': np.random.choice(categories, 300),
    'X': np.random.rand(300),
    'Y': np.random.rand(300) * 10
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Loop through categories and create scatter plots
for category in categories:
    # Filter data for the current category
    subset = df[df['Category'] == category]

    # Create a new figure
    plt.figure(figsize=(8, 6))

    # Generate the scatter plot
    sns.scatterplot(x='X', y='Y', data=subset)

    # Set the title and labels
    plt.title(f'Scatter Plot for {category}')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')

    # Display the plot
    plt.show()
