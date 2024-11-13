# Customized Boxplot
sns.set(style="whitegrid")
sns.boxplot(x='Department', y='Salary', hue='Position', data=data, palette="Set3")
plt.title('Salary Distribution Across Departments and Positions')
plt.xlabel('Department')
plt.ylabel('Salary ($)')
plt.show()
