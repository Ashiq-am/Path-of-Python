from calendar import c


def data_entry(conn=None):
	number = +8801980536706
	name = "ASHIQ"
	c.execute("INSERT INTO RecordONE (Number, Name) VALUES(?, ?)",
												(number, name))

	conn.commit()
