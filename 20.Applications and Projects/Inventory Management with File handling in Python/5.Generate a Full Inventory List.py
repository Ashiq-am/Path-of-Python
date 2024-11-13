def generate_inventory():
	with open('inventory.txt', 'r') as file:
		inventory_data = file.readlines()
	inventory_text = '\n'.join(inventory_data)
	result_label.config(text=inventory_text)
