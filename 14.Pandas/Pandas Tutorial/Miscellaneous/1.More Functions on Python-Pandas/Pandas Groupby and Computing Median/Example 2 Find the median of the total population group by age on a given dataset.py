# import packages
import pandas as pd

# read Dataset
data = pd.read_csv("WorldPopulationByAge2020.csv")
data.head()

# perform group by AgeGrp and find median
data.groupby(["AgeGrp"])["PopTotal"].median()
