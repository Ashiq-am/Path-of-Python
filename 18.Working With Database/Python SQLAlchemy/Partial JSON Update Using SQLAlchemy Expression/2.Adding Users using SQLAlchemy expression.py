# Importing required modules
from main import User, Session, engine

# Create a session
local_session = Session(bind=engine)

# Store table data to the variable
user1 = User(id=1, username="aditya",
			info={'dob': '21', 'subject': 'math'})
user2 = User(id=2, username="timmy",
			info={'dob': '22', 'subject': 'science'})
user3 = User(id=3, username="sushant",
			info={'dob': '23', 'subject': 'programming'})

# Add data to the session
local_session.add(user1)
local_session.add(user2)
local_session.add(user3)

# Perform the changes to the database.
local_session.commit()

# Retrieve data and print it
result = local_session.query(User).\
	filter(User.id == "1").first()
print(result)
