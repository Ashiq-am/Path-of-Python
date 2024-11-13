# Check if a person with age 30 exists in the list
target_age = 30
found = False

for person in people:
	if person.age == target_age:
		found = True
		break

if found:
	print(f"A person with age {target_age} exists in the list.")
else:
	print(f"No person with age {target_age} found in the list.")
