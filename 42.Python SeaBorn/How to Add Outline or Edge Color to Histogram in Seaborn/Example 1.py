# import required modules
import seaborn
from vega_datasets import data

# assign dataset
dataset = data.co2_concentration()

# display dataset
dataset.sample(n=5)
