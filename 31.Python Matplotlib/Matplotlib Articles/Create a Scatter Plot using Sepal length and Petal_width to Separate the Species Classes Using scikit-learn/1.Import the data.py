# importing packages
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sns

# loading data
iris = pd.read_csv("iris.csv")
print(iris.head())
