# Group by 'day' and 'sex' and calculate the size of each group
grouped_data = tips.groupby(['day', 'sex']).size().reset_index(name='counts')

# Calculate the total counts for each day
grouped_data['total'] = grouped_data.groupby('day')['counts'].transform('sum')

# Calculate the proportion of each category
grouped_data['proportion'] = grouped_data['counts'] / grouped_data['total']
grouped_data
