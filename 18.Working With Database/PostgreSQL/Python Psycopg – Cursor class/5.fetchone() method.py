sql = '''SELECT * FROM employee;'''

# executing the sql command
cursor.execute(sql)

# fetching one row
result = cursor.fetchone()

print(result)
