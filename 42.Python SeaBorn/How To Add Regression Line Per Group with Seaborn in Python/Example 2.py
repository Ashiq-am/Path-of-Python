# import libraries
import seaborn

# load data
tip = seaborn.load_dataset('tips')

# use lmplot
seaborn.lmplot(x="total_bill",
			y="tip",
			hue="day",
			markers='*',
			data=tip)
