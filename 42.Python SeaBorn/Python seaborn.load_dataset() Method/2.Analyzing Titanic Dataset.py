import seaborn as sns

# Load Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Visualize survival rate by class
sns.barplot(x='class', y='survived', data=titanic_df)
