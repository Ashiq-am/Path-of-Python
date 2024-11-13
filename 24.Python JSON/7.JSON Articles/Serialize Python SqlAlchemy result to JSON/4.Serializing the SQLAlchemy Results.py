# Serialize a single user
user = session.query(User).first()
user_json = json.dumps(user, cls=AlchemyEncoder)
print(user_json)

# Serialize all users
users = session.query(User).all()
users_json = json.dumps(users, cls=AlchemyEncoder)
print(users_json)
