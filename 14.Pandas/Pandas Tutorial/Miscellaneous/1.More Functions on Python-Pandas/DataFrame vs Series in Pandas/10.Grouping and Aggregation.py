# Grouping by a column and calculating mean
avg_age_by_city = df.groupby('City')['Age'].mean()
print(avg_age_by_city)
