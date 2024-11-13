# import required modules
import seaborn
from vega_datasets import data

# assign dataset
dataset = data.la_riots()

# display dataset
dataset.sample(n=5)
