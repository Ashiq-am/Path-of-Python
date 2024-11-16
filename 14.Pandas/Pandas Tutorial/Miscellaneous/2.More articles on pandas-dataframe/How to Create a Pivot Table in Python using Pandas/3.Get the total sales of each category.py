# creating pivot table of total
# sales category-wise aggfunc = 'sum'
# will allow you to obtain the sum of
# sales each product
pivot = df.pivot_table(index =['Category'],
					values =['Amount'],
					aggfunc ='sum')
print(pivot)
