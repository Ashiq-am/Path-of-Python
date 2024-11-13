import seaborn as sns

# Load Tips dataset
tips_df = sns.load_dataset('tips')

# Visualize tip distribution by day and time
sns.violinplot(x='day', y='tip', hue='time', data=tips_df, split=True)
