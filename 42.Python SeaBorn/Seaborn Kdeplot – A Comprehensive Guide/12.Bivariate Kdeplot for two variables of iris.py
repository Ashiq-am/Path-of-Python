setosa = iris.loc[iris.species=="setosa"]
virginica = iris.loc[iris.species == "virginica"]
sns.kdeplot(setosa.petal_length, setosa.petal_width)
