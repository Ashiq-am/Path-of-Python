# importing packages
import altair
import altair_catplot
import seaborn

# load data
tip = seaborn.load_dataset('tips')

# draw a plot
altair_catplot.catplot(tip,
					transform ='jitterbox',
					mark ='point',
					encoding = dict(x = altair.X('time:N', title = None),
									y = altair.Y('total_bill:Q', scale = altair.Scale(zero = False)),
									color = altair.Color('time:N', legend = None))
					)
