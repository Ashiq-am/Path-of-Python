# creating pivot table of total sales
# product-wise aggfunc = 'sum' will
# allow you to obtain the sum of sales
# each product
pivot = df.pivot_table(index =['Product'],
					values =['Amount'],
					aggfunc ='sum')
print(pivot)
