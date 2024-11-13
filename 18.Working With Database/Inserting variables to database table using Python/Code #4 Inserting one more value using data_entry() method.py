def data_entry():
	number = 4321
	name = "Author"
	c.execute("INSERT INTO RecordONE (Number, Name) VALUES(?, ?)", (number, name))
	conn.commit()
