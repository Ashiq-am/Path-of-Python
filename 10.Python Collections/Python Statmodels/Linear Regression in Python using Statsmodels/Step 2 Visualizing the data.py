# import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('headbrain1.csv')
sns.regplot('Head Size(cm^3)', 'Brain Weight(grams)', data=df)

plt.show()
