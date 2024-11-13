# import Row
from pyspark.sql import Row

dic_1 = {'First_name':"Sravan",
		'Last_name':"Kumar",
		'address':"hyderabad"}

dic_2 = {'First_name':"Bobby",
		'Last_name':"Gottumukkala",
		'address':"Ponnur"}

# create two rows with
# three values as dictionary.
row = [Row(dic_1),
	Row(dic_2)]
# display row
print(row)
