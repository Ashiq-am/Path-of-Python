# Sample DataFrame with subgroups
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Values': [10, 12, 15, 20, 22, 19],
    'Subgroup': ['X', 'Y', 'X', 'Y', 'X', 'Y']
}

df = pd.DataFrame(data)

# Split the violins by subgroup
sns.violinplot(x='Group', y='Values', hue='Subgroup', data=df, split=True)
plt.show()
