class SharedList:
	shared_list = []

# Append an element by reference
SharedList.shared_list.append(42)

# Accessing the updated list
print(SharedList.shared_list)
