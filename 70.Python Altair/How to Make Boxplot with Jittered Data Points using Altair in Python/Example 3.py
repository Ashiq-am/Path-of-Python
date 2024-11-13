# importing packages
import altair
import altair_catplot
import seaborn

# load data
iris = seaborn.load_dataset('iris')

# draw a plot
altair_catplot.catplot(iris,
					transform ='jitterbox',
					mark ='circle',
					encoding = dict(x = altair.X('species:N', title = None),
									y = altair.Y('sepal_length:Q', scale = altair.Scale(zero = False)),
									color = altair.Color('species:N', legend = None))
					)
