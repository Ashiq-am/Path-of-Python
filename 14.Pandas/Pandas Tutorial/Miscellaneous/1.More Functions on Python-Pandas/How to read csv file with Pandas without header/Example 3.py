# importing python package
import pandas as pd

# read the content of csv file
dataset = pd.read_csv("sample1.csv", header=None)

# display modified csv file
display(dataset)
