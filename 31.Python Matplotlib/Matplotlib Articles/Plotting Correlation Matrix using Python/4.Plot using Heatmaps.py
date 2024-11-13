import seaborn as sns

# checking correlation using heatmap
#Loading dataset
flights = sns.load_dataset("flights")

#ploting the heatmap for correlation
ax = sns.heatmap(flights.corr(), annot=True)
