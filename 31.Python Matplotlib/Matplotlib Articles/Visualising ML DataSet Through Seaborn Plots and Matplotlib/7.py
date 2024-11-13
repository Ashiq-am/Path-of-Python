# importing the modules and dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("Survival.csv")

# showing that there are more Male's Between Age Of 12-40
dataset.Gender[((dataset["Age"] >= 12) &
				(dataset["Age"] <= 40)) &
			(dataset["Gender"] == "Male")].count()
dataset.Gender[((dataset["Age"] >= 12) &
				(dataset["Age"] <= 40)) &
			(dataset["Gender"] == "Female")].count()
