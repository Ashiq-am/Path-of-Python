# import module
import numpy as np
import pandas as pd

# reading csv file
dataset = pd.read_csv("diamonds.csv")

# printing first 5 rows
print(dataset.head(5))
