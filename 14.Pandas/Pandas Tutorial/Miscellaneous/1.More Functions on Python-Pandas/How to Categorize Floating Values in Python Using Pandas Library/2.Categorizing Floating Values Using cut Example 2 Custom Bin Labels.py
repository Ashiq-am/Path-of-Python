# Define custom bin labels
bin_labels = ['Very Low', 'Low', 'Medium', 'High', 'Very High']

# Categorize with custom labels
df['Categories'] = pd.cut(df['Values'], bins, labels=bin_labels)

print(df)
