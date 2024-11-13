query = "SELECT * FROM employee;"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)
