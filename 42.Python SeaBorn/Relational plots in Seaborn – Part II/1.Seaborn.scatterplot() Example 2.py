import seaborn as sns


iris = sns.load_dataset("iris")

sns.scatterplot(x = iris.sepal_length,
				y = iris.sepal_width,
				hue = iris.species,
				style = iris.species)
