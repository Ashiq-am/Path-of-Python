import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data1 = sns.load_dataset('iris').query("species == 'setosa'")['petal_length']
data2 = sns.load_dataset('iris').query("species == 'versicolor'")['petal_length']

# Plotting overlapping histograms
sns.histplot(data=data1, color='blue', alpha=0.5, label='Setosa')
sns.histplot(data=data2, color='orange', alpha=0.5, label='Versicolor')

# Adding labels and legend
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.legend()

plt.show()
