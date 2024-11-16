# creating pivot table of Mean, Median,
# Minimum sale by category aggfunc = {'median',
# 'mean', 'min'} will get median, mean and
# minimum of sales respectively
pivot = df.pivot_table(index =['Category'], values =['Amount'],
					aggfunc ={'median', 'mean', 'min'})
print (pivot)
