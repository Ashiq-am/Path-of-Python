# Insert values

# Create user objects
user1 = User(name='John')
user2 = User(name='Smith')
user3 = User(name='Peter')

# Add user objects to session
session.add(user1)
session.add(user2)
session.add(user3)

# Commit the changes to the database
session.commit()
