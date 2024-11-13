# Querying the table
select_st = select([Employee])
result = engine.execute(select_st)

# Print column names
print(result.keys())

# Print rows
for row in result:
	print(row)
