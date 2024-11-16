# import the required library
import inline as inline
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#matplotlib_inline


# load the dataset
df = pd.read_csv("tips.csv")

# display 5 rows of dataset
df.head()
