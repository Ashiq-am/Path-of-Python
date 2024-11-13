import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load example dataset
iris = sns.load_dataset('iris')

# Define subsets of features
feature_subsets = [
    ['sepal_length', 'sepal_width'],
    ['petal_length', 'petal_width']
]

# Loop through feature subsets and create pair plots
for subset in feature_subsets:
    # Create a new figure
    plt.figure(figsize=(8, 6))

    # Generate the pair plot
    sns.pairplot(iris, vars=subset, hue='species')

    # Set the title
    plt.suptitle(f'Pair Plot for Features: {", ".join(subset)}', y=1.02)

    # Display the plot
    plt.show()
