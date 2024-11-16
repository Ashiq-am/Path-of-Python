# Define custom quantile labels
quantile_labels = ['Q1', 'Q2', 'Q3', 'Q4']

# Categorize with custom quantile labels
df['Quantile Categories'] = pd.qcut(df['Values'], 4, labels=quantile_labels)

print(df)
