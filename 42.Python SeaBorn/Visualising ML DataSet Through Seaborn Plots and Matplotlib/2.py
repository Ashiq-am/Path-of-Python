# importing the modules and dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("Survival.csv")

# Checking the count of Age Group 20-40
dataset.Age[(dataset["Age"] >= 20) & (dataset["Age"] <= 40)].count()
