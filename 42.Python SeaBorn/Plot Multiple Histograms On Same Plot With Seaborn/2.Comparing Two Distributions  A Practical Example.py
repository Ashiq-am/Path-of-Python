import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data1 = sns.load_dataset('titanic').query("`class` == 'First'")['age'].dropna()
data2 = sns.load_dataset('titanic').query("`class` == 'Third'")['age'].dropna()

# Plotting overlapping histograms with KDE
sns.histplot(data=data1, color='blue', alpha=0.5, kde=True, label='First Class')
sns.histplot(data=data2, color='orange', alpha=0.5, kde=True, label='Third Class')

# Adding labels and legend
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend()

plt.show()
