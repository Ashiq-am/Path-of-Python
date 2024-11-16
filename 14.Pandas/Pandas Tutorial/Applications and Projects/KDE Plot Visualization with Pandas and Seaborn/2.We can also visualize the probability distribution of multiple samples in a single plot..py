# Plotting the KDE Plot
sns.kdeplot(iris_setosa['Sepal_Length'],
			iris_setosa['Sepal_Width'],
			color='r', shade=True, Label='Iris_Setosa',
			cmap="Reds", shade_lowest=False)

sns.kdeplot(iris_virginica['Sepal_Length'],
			iris_virginica['Sepal_Width'], color='b',
			shade=True, Label='Iris_Virginica',
			cmap="Blues", shade_lowest=False)
