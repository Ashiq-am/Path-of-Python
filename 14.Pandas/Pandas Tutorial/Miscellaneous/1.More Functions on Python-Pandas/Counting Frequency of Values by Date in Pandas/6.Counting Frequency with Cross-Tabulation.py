# Cross-tabulation to count frequency by Date and Value
crosstab_counts = pd.crosstab(df['date'], df['value'])

print(crosstab_counts)
