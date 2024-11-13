""

'''Create a new dataframe called masterDisciplines in which we will 
insert this new set of people and then create a visualization with it'''



masterDisciplines = goldMedals['Sport'][goldMedals['Age'] > 50]
plt.figure(figsize=(20, 10))
plt.tight_layout()
sns.countplot(masterDisciplines)
plt.title('Gold Medals for Athletes Over 50')
plt.show()
