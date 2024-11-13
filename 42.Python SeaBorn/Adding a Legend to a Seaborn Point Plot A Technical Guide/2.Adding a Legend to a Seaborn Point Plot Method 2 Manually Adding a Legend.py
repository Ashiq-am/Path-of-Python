import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.DataFrame({'date': pd.date_range(start='1/1/2020', periods=4), 'count': [35, 43, 12, 27]})
df2 = pd.DataFrame({'date': pd.date_range(start='1/1/2020', periods=4), 'count': [25, 33, 22, 17]})
df3 = pd.DataFrame({'date': pd.date_range(start='1/1/2020', periods=4), 'count': [45, 53, 32, 37]})

# Plotting multiple dataframes
plt.figure(figsize=(10, 6))
sns.pointplot(x='date', y='count', data=df1, color='blue', label='Dataset 1')
sns.pointplot(x='date', y='count', data=df2, color='green', label='Dataset 2')
sns.pointplot(x='date', y='count', data=df3, color='red', label='Dataset 3')

# Adding legend
plt.legend(title='Datasets')
plt.show()
