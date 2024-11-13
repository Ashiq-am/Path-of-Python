def get_title(user_id):
    if user_id == 1:
        return "Admin"
    else:
        return None
user_id = 2
title = get_title(user_id)
# Fix using string formatting
message = f"User Title: {title if title is not None else 'Unknown'}"
print(message)
