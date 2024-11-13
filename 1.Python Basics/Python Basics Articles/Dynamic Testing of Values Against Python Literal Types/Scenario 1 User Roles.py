# code
UserRole = Literal['admin', 'user', 'guest']

def is_user_role(value) -> bool:
    return is_literal_value(value, UserRole)

print(is_user_role('admin'))
print(is_user_role('moderator'))
