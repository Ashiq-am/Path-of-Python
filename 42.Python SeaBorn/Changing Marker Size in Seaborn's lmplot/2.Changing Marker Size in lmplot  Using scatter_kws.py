import seaborn as sns
import pandas as pd

df = sns.load_dataset("tips")

# Change marker size using scatter_kws
sns.lmplot(x="total_bill", y="tip", data=df, scatter_kws={"s": 100})
