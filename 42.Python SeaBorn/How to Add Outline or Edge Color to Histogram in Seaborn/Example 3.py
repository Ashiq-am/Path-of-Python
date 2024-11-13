# import required modules
import seaborn
from vega_datasets import data

# assign dataset
dataset = data.seattle_weather()

# display dataset
dataset.sample(n=5)

# depict illustration
sns.distplot(dataset['temp_min'],
			hist_kws={'color': 'black', 'edgecolor': 'green',
					'linewidth': 5})
