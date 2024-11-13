import tkinter as tk
from tkinter import ttk

def tab_selected(event):
    notebook = event.widget
    tab_id = notebook.select()
    tab_text = notebook.tab(tab_id, 'text')
    print(f"Selected Tab Text: {tab_text}")

root = tk.Tk()
root.title("TTK Notebook")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')

notebook.bind("<<NotebookTabChanged>>", tab_selected)

root.mainloop()
