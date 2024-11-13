# Customizing Vertical Grid Lines
sns.set(style="whitegrid")
ax = sns.boxplot(x='Department', y='Salary', hue='Position', data=data, palette="Set1")
plt.grid(True, axis='x', linestyle='--', linewidth=0.7, color='gray')
plt.title('Customized Vertical Grid Lines in Grouped Boxplot')
plt.xlabel('Department')
plt.ylabel('Salary ($)')
plt.show()
