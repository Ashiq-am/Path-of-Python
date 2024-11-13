sql = '''SELECT * FROM employee;'''

# executing the sql command
cursor.execute(sql)

# fetching first two rows
result = cursor.fetchmany(2)

print(result)
