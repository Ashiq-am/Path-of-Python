# importing the libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# loading the dataset
# from seaborn library
data = sns.load_dataset('car_crashes')

# viewing the dataset
print(data.head(4))
