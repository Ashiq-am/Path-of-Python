# if condition with column conditions given
# the condition is if MRP of the product <= 2000
# and discount > 0 show me those items
df[(df['MRP'] <= 2000) & (df['Discount'] > 0)]
