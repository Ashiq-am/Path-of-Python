import tkinter as tk

def get_entry_value(event):
    value = entry.get()
    print("Entry value:", value)

# Create the Tkinter window
window = tk.Tk()
window.title("Entry Widget Value Retrieval")

# Create an Entry widget
entry = tk.Entry(window)
entry.pack()

# Bind the return key press event to get_entry_value function
entry.bind("<Return>", get_entry_value)

# Start the Tkinter event loop
window.mainloop()
