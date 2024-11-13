import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
df = sns.load_dataset("titanic")

# Drop missing values in fare and pclass for simplicity
df = df.dropna(subset=['fare', 'pclass'])
