class Event(db.Model):
	date = mapped_column(db.String, primary_key=True)
	event = mapped_column(db.String)
