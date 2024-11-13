sns.set_palette("pastel")
sns.lineplot(data=df, x='day', y='sales', hue='store')
