# Python3 code to update records in a database

# Print records before updation
cursor = cnt.execute('''SELECT * FROM gfg''')
print('Before Updation')
for i in cursor:
	print(i[0]+" "+str(i[1])+" "+str(i[2]))

print('') # print a newline

# Execute an Update statement
cnt.execute('''UPDATE gfg SET POINTS=POINTS+5 WHERE
POINTS<20;''')

cursor = cnt.execute('''SELECT * FROM gfg''')
print('After Updation')
for i in cursor:
	print(i[0]+" "+str(i[1])+" "+str(i[2]))
