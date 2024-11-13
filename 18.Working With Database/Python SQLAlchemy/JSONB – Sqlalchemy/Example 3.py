# Fetch the data
select_stmt = users.select()
result = conn.execute(select_stmt)
row = result.fetchone()
print(row)
