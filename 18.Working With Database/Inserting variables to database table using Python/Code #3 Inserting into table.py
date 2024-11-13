def data_entry():
	number = 1234
	name = "GeeksforGeeks"
	c.execute("INSERT INTO RecordONE (Number, Name) VALUES(?, ?)",
												(number, name))

	conn.commit()
