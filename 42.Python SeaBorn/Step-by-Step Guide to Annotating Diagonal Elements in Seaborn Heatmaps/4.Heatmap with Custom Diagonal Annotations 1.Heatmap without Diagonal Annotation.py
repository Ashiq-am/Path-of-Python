import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the iris dataset
iris = sns.load_dataset('iris')

# Exclude non-numeric columns ('species') from the correlation matrix
numeric_columns = iris.drop(columns=['species'])
corr_matrix = numeric_columns.corr()

# Plot the heatmap without diagonal annotation
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap (Without Diagonal Annotation)')
plt.show()
