# importing useful libraries
import seaborn as sns
import matplotlib.pyplot as plt

# using titanic dataset from
# seaborn library
df = sns.load_dataset("titanic")

# to see first 5 rows of dataset
print(df.head())
