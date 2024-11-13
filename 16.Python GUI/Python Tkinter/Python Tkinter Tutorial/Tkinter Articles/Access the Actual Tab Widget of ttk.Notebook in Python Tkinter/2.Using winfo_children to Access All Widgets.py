import tkinter as tk
from tkinter import ttk

def approach2():
    for i, tab in enumerate(notebook.winfo_children()):
        tab_text = notebook.tab(i, 'text')
        print(f"Tab {i} Text: {tab_text}")

root = tk.Tk()
root.title("TTK Notebook Example")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')

approach2()

root.mainloop()
