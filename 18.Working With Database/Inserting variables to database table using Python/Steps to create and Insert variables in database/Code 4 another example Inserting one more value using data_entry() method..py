from this import c


def data_entry(conn=None): 
	number = 4321
	name = "Author"
	c.execute("INSERT INTO RecordONE (Number, Name) VALUES(?, ?)", (number, name)) 
	conn.commit() 
