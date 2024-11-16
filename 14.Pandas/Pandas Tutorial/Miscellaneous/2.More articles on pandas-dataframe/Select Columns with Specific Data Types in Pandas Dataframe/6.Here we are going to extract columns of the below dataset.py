# import required module
import pandas as pd
from vega_datasets import data

# assign dataset
df = data.seattle_weather()

# display dataset
df.sample(10)
