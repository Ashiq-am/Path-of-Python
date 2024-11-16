# Group DataFrame by 'City' column and convert to nested JSON
grouped_data = df.groupby('City').apply(lambda x: x[['Name', 'Age']].to_json(orient='records'))

# Print the grouped data
print(grouped_data)
