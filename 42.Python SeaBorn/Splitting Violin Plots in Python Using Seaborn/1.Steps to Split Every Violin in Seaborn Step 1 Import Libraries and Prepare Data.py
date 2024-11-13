import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load sample dataset
tips = sns.load_dataset("tips")

# Display the first few rows of the dataset
print(tips.head())
