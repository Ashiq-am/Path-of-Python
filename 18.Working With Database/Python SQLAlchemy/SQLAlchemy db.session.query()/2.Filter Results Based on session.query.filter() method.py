from sqlalchemy import and_, or_
# Use multiple mathematical equations as filters in a query
# Use a mathematical equation as a filter in a query
results = session.query(Example).filter(Example.value * 2 > 3).all()
for result in results:
	print(result.id, result.value)
