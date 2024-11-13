def add_inventory():
	item_name = item_name_entry.get()
	item_qty = int(item_qty_entry.get())
	with open('inventory.txt', 'a') as file:
		file.write(f'{item_name},{item_qty}\n')
	item_name_entry.delete(0, tk.END)
	item_qty_entry.delete(0, tk.END)
