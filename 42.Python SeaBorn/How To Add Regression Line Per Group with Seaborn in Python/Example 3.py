# import libraries
import seaborn

# load data
iris = seaborn.load_dataset('iris')

# use lmplot
seaborn.lmplot(x="sepal_length",
			y="sepal_width",
			hue="species",
			markers='+',
			data=iris)
