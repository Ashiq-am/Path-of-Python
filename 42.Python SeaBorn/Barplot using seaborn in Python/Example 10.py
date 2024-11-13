# importing the required library
import seaborn as sns
import matplotlib.pyplot as plt

# read a titanic.csv file
# from seaborn libraray
df = sns.load_dataset('titanic')

sns.barplot(x="class", y="fare", data=df,
				linewidth=2.5, facecolor=(1, 1, 1, 0),
				errcolor=".2", edgecolor=".2")
