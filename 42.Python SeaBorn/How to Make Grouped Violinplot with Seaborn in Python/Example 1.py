import seaborn as sns
import pandas as pd


datasets = sns.load_dataset('iris')

datasets.head()

sns.violinplot(datasets['sepal_length'])
