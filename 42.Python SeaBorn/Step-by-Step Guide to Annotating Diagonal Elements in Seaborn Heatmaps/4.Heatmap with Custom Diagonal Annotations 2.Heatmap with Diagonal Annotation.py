import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the iris dataset
iris = sns.load_dataset('iris')

# Exclude non-numeric columns ('species') from the correlation matrix
numeric_columns = iris.drop(columns=['species'])
corr_matrix = numeric_columns.corr()

# Plot the heatmap with diagonal annotation
plt.figure(figsize=(8, 6))
ax = sns.heatmap(corr_matrix, cmap='coolwarm')

# Annotate diagonal elements
for i in range(len(corr_matrix)):
    ax.text(i + 0.5, i + 0.5, f'{corr_matrix.iloc[i, i]:.2f}',
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=10, color='black')

plt.title('Correlation Matrix Heatmap with Diagonal Annotation')
plt.show()
