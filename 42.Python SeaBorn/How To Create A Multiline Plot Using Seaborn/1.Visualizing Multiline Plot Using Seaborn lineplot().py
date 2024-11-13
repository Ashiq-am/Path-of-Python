import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Year': [2010, 2011, 2012, 2013, 2014],
    'A': [50, 40, 30, 60, 10],
    'B': [10, 20, 25, 42, 12],
    'C': [20, 30, 40, 50, 60]
})

# plot multiple lines
sns.lineplot(data=df, x='Year', y='A', label='A')
sns.lineplot(data=df, x='Year', y='B', label='B')
sns.lineplot(data=df, x='Year', y='C', label='C')
plt.legend()
plt.show()
