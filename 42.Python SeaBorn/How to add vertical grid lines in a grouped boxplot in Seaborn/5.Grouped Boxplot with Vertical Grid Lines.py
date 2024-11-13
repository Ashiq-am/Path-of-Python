# Load Titanic dataset
titanic = sns.load_dataset('titanic')

# Grouped Boxplot with Vertical Grid Lines
sns.set(style="whitegrid")
ax = sns.boxplot(x='class', y='fare', hue='sex', data=titanic, palette="Set3")
plt.grid(True, axis='x', linestyle='--', linewidth=0.7, color='gray')
plt.title('Fare Distribution by Class and Gender (Titanic)')
plt.xlabel('Class')
plt.ylabel('Fare ($)')
plt.show()
