list_of_db = client.list_database_names()

if "mydbase" in list_of_db:
	print("Exists !!")
