# import Row
from pyspark.sql import Row

# dict
dic = {'First_name':"Sravan",
	'Last_name':"Kumar",
	'address':"hyderabad"}

# create a row with three values
# as dictionary.
row = Row(dic)

# display row
print(row)
