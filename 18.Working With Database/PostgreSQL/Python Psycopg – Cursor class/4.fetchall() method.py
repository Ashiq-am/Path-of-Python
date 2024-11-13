sql = '''SELECT * FROM employee;'''

# executing the sql command
cursor.execute(sql)

# fetching all the rows
results = cursor.fetchall()
print(results)
