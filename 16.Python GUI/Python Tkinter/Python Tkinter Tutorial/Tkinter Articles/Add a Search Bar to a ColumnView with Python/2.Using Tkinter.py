import tkinter as tk
from tkinter import ttk

class GFG(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Search ColumnView')

        # Create search bar
        self.search_var = tk.StringVar()
        self.search_var.trace('w', self.filter_items)
        self.search_entry = ttk.Entry(self, textvariable=self.search_var)
        self.search_entry.pack()

        # Create ColumnView
        self.column_view = ttk.Treeview(self)

        # Populate ColumnView with items
        # Replace this with your own data population logic
        for i in range(10):
            self.column_view.insert('', 'end', text=f'Item {i}')
        self.column_view.pack()

    def filter_items(self, *args):
        search_query = self.search_var.get()


if __name__ == '__main__':
    app = GFG()
    app.mainloop()
