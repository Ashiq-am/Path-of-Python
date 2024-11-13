# Importing required modules
from sqlalchemy import update, func
from main import User, Session, engine

# Creates a session
local_session = Session(bind=engine)

# Declare variables
value = 'programming'
id = 1

# Update the JSON column data
update_table = local_session.query(User).\
	filter(User.id == id).update({
		'info': func.json_set(
			User.info,
			"$.subject",
			value
		)
	}, synchronize_session='fetch')

# Commit the changes in database
local_session.commit()
