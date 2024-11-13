# Initial code with potential error
def get_user_name(user_id):
    users = {1: "Alice", 2: "Bob", 3: None}
    return users.get(user_id)
user_id = 3
message = get_user_name(user_id) + " has logged in."
# Fixing the error
def get_user_name(user_id):
    users = {1: "Alice", 2: "Bob", 3: None}
    return users.get(user_id)
user_id = 3
user_name = get_user_name(user_id)
if user_name is not None:
    message = user_name + " has logged in."
else:
    message = "Unknown user has logged in."
print(message)
