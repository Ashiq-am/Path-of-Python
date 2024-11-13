import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Creating a larger sample dataset
data = pd.DataFrame({
    'Department': ['Sales', 'Sales', 'Sales', 'HR', 'HR', 'HR', 'IT', 'IT', 'IT', 'Marketing', 'Marketing', 'Marketing'] * 2,
    'Position': ['Junior', 'Mid', 'Senior', 'Junior', 'Mid', 'Senior', 'Junior', 'Mid', 'Senior', 'Junior', 'Mid', 'Senior'] * 2,
    'Salary': [42000, 52000, 62000, 48000, 54000, 67000, 45000, 55000, 68000, 43000, 51000, 63000,
               44000, 53000, 60000, 47000, 56000, 70000, 46000, 57000, 69000, 42000, 54000, 65000]
})

# Grouped Boxplot
sns.set(style="whitegrid")
sns.boxplot(x='Department', y='Salary', hue='Position', data=data)
plt.title('Salary Distribution by Department and Position')
plt.xlabel('Department')
plt.ylabel('Salary ($)')
plt.show()
