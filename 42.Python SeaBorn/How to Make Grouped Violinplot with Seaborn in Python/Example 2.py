import seaborn as sns
import pandas as pd


datasets = sns.load_dataset('iris')

datasets.head()

sns.violinplot(x='species', y='sepal_width', data=datasets,
			inner="quart", linewidth=1)
