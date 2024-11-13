import seaborn as sns
import pandas as pd

df = sns.load_dataset("tips")
sns.lmplot(x="total_bill", y="tip", data=df)
