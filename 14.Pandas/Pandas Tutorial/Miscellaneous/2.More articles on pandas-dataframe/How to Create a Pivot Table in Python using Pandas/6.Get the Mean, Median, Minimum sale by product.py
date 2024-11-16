# creating pivot table of Mean, Median,
# Minimum sale by product aggfunc = {'median',
# 'mean', 'min'} will get median, mean and
# minimum of sales respectively
pivot = df.pivot_table(index =['Product'], values =['Amount'],
					aggfunc ={'median', 'mean', 'min'})
print (pivot)
