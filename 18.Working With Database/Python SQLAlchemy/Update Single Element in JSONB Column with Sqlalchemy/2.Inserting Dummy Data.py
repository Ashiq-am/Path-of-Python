# Define the insert query with the data you want to insert in the table
insert_query = employeest.insert().values(id=10, info={
	"name": "Jon",
	"age": 33,
	"job": {"title": "Software Engineer", "level": "three"}
})
print(insert_query)
conn = engine.connect()
result = conn.execute(insert_query)
print('Insert query results:', result.rowcount)
conn.commit()
