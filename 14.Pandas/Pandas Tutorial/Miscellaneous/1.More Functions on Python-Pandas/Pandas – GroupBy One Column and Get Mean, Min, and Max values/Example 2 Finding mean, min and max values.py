# using groupby function with aggregation
# to get mean, min and max values
result = sales_data.groupby('salesman_id').agg({'purchase_amt': ['mean', 'min', 'max']})

print("Mean, min, and max values of Purchase Amount grouped by Salesman id")
print(result)
