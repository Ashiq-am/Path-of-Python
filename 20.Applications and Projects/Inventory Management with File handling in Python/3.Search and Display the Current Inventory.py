def search_inventory():
	search_name = item_name_entry.get()
	with open('inventory.txt', 'r') as file:
		for line in file:
			name, qty = line.strip().split(',')
			if name == search_name:
				result_label.config(text=f'{name} - {qty}')
				return
	result_label.config(text=f'{search_name} not found in inventory.')
	item_name_entry.delete(0, tk.END)
