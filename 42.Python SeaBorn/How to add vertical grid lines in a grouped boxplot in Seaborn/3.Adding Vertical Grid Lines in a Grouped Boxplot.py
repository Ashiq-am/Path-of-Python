# Adding Vertical Grid Lines
sns.set(style="whitegrid")
ax = sns.boxplot(x='Department', y='Salary', hue='Position', data=data, palette="Set2")
plt.grid(True, axis='x')  # Enable vertical grid lines
plt.title('Salary Distribution with Vertical Grid Lines')
plt.xlabel('Department')
plt.ylabel('Salary ($)')
plt.show()
