def update_inventory():
	item_name = item_name_entry.get()
	item_qty = int(item_qty_entry.get())
	with open('inventory.txt', 'r') as file:
		inventory_data = file.readlines()
	with open('inventory.txt', 'w') as file:
		for line in inventory_data:
			name, qty = line.strip().split(',')
			if name == item_name:
				file.write(f'{name},{item_qty}\n')
			else:
				file.write(line)
	item_name_entry.delete(0, tk.END)
	item_qty_entry.delete(0, tk.END)
