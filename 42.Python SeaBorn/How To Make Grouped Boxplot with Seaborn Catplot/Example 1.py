import pandas as pd
import seaborn as sns


df = pd.read_csv("titanic_train.csv")
df.dropna()
sns.catplot(x='Sex', y='Fare', hue='Survived',
			data=df, height=9, kind="box")
