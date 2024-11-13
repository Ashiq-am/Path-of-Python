import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing

df = pd.read_csv("titanic_train.csv")
df.dropna()

le = preprocessing.LabelEncoder()
df["Sex"] = le.fit_transform(df["Sex"])


rp = sns.FacetGrid(df, row="Sex", hue="Sex", aspect=5, height=1.25)

rp.map(sns.kdeplot, 'Survived', clip_on=False,
	shade=True, alpha=0.7, lw=4, bw=.2)

rp.map(plt.axhline, y=0, lw=4, clip_on=False)
