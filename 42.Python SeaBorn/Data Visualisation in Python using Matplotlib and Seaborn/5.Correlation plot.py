# Finding and plotting the correlation for
# the independent variables

# import required module
import seaborn as sns

# adjust plot
sns.set(rc={'figure.figsize': (14, 5)})

# assign data
ind_var = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
		'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']

# illustrate heat map.
sns.heatmap(diabetes.select_dtypes(include='number').corr(),
			cmap=sns.cubehelix_palette(20, light=0.95, dark=0.15))
