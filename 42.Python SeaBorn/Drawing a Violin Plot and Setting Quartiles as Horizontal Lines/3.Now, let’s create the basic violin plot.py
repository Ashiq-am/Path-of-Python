plt.figure(figsize=(8, 6))
sns.violinplot(x='Category', y='Values', data=data, inner=None)
plt.title('Violin Plot with Quartiles as Horizontal Lines')
plt.show()
