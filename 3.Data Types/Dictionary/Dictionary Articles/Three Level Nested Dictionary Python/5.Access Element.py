# Accessing elements
person_name = contact_details['person_id']['name']
home_phone = contact_details['person_id']['phone']['home']
email = contact_details['person_id']['email']

print(f"Name: {person_name}")
print(f"Home Phone: {home_phone}")
print(f"Email: {email}\n")
