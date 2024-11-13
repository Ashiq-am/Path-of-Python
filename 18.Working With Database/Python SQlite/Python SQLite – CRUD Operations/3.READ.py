# Python3 code to read data from a table

print('Name, Points and Accuracy from '
	'records with accuracy greater than 85')

cursor = cnt.execute('''SELECT * FROM gfg WHERE ACCURACY>85;''')

# print data using the cursor object
for i in cursor:
	print(i[0]+" "+str(i[1])+" "+str(i[2]))

print('') # Print new line

print('Name, Accuracy from '
	'records with accuracy greater than 85')

cursor = cnt.execute('''SELECT NAME, ACCURACY FROM
gfg WHERE ACCURACY>85;''')

# print data using the cursor object
for i in cursor:
	print(i[0]+" "+str(i[1]))
