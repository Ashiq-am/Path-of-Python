# Create sample data
user1 = User(name="John Doe", email="john.doe@example.com")
user2 = User(name="Jane Smith", email="jane.smith@example.com")
session.add_all([user1, user2])
session.commit()
