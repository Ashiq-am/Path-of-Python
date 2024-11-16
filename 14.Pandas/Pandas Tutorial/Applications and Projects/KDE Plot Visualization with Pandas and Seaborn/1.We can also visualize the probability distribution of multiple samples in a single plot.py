# Plotting the KDE Plot
sns.kdeplot(iris_df.loc[(iris_df['Target']=='Iris_Setosa'),
			'Sepal_Length'], color='r', shade=True, Label='Iris_Setosa')

sns.kdeplot(iris_df.loc[(iris_df['Target']=='Iris_Virginica'),
			'Sepal_Length'], color='b', shade=True, Label='Iris_Virginica')

plt.xlabel('Sepal Length')
plt.ylabel('Probability Density')
