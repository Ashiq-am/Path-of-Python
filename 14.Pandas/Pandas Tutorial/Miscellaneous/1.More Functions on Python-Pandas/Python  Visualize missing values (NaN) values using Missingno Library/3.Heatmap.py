# Program to visualize missing values in dataset

# Importing the libraries
import pandas as pd
import missingno as msno

# Loading the dataset
df = pd.read_csv("kamyr-digester.csv")


# Visualize the correlation between the number of
# missing values in different columns as a heatmap
msno.heatmap(df)
