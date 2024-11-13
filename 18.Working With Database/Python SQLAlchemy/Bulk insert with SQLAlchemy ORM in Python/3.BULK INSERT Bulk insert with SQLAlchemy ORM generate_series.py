engine.execute("INSERT INTO students (id, name, lastname)\
			SELECT gt,'Scott Derrickson','Derrickson'\
			FROM generate_series(4,10) as gt")

