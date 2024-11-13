# executing the sql statement
cursor.executemany("INSERT INTO classroom VALUES(%s,%s,%s)",
				values)
