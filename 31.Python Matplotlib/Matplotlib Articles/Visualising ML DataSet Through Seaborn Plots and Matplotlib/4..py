# importing the modules and dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("Survival.csv")

# Checking The Variation Between Fare And Age
dataset.Age[((dataset["Fare"] >= 100) &
			(dataset["Fare"]<=200)) &
			((dataset["Age"]>=20) &
			dataset["Age"]<=40)].count()
