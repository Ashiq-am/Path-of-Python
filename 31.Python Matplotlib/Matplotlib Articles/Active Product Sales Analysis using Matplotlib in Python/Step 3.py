# n =24 in this case, can be modified
# as per need to see top 'n' busiest hours
timemost1 = Order_Details['Hour'].value_counts().index.tolist()[:24]

timemost2 = Order_Details['Hour'].value_counts().values.tolist()[:24]
