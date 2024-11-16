# creating pivot table of sales
# by product and category both
# aggfunc = 'sum' will allow you
# to obtain the sum of sales each
# product
pivot = df.pivot_table(index =['Product', 'Category'],
					values =['Amount'], aggfunc ='sum')
print (pivot)
