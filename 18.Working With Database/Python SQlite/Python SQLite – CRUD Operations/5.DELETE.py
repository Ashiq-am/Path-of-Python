# Python3 code to delete records from database

# Print records before deletion
cursor = cnt.execute('''SELECT * FROM gfg''')
print('Before Deletion')
for i in cursor:
	print(i[0]+" "+str(i[1])+" "+str(i[2]))

print('') # print a newline

# Execute a delete statement
cnt.execute('''DELETE FROM gfg WHERE ACCURACY>91;''')

cursor = cnt.execute('''SELECT * FROM gfg''')
print('After Deletion')
for i in cursor:
	print(i[0]+" "+str(i[1])+" "+str(i[2]))
