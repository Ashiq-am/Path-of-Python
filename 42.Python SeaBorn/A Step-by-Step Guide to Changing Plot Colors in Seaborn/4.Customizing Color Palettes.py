custom_palette = ['#FF6347', '#4682B4']
sns.lineplot(data=df, x='day', y='sales', hue='store', palette=custom_palette)
