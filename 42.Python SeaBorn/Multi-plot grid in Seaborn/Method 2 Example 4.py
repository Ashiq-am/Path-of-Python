import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


fig, axes = plt.subplots(2, 3, figsize=(18, 10))

fig.suptitle('Geeksforgeeks - 2 x 3 axes Box plot with data')

iris = sns.load_dataset("iris")

sns.boxplot(ax=axes[0, 0], data=iris, x='species', y='petal_width')
sns.boxplot(ax=axes[0, 1], data=iris, x='species', y='petal_length')
sns.boxplot(ax=axes[0, 2], data=iris, x='species', y='sepal_width')
sns.boxplot(ax=axes[1, 0], data=iris, x='species', y='sepal_length')
sns.boxplot(ax=axes[1, 1], data=iris, x='species', y='petal_width')
sns.boxplot(ax=axes[1, 2], data=iris, x='species', y='petal_length')
