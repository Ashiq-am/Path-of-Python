# import the required library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from docutils.nodes import inline
matplotlib
inline


# load the dataset
df = pd.read_csv("tips.csv")

# display 5 rows of dataset
df.head()
