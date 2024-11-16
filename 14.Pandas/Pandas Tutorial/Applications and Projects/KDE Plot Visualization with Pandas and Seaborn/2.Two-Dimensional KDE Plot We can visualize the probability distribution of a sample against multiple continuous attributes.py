# Setting up the samples
iris_setosa = iris_df.query("Target=='Iris_Setosa'")
iris_virginica = iris_df.query("Target=='Iris_Virginica'")

# Plotting the KDE Plot
sns.kdeplot(iris_setosa['Sepal_Length'],
			iris_setosa['Sepal_Width'],
			color='r', shade=True, Label='Iris_Setosa',
			cmap="Reds", shade_lowest=False)
