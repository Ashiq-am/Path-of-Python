# importing libraries
import seaborn as sb

# load data
df = sb.load_dataset('iris')

# use lmplot
sb.lmplot(x = "sepal_length",
			y = "petal_length",
			ci = None,
			data = df)
