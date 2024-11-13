import tkinter as tk

def disable_button():
    button['state'] = tk.DISABLED

def enable_button():
    button['state'] = tk.NORMAL

# Create the main window
root = tk.Tk()
root.title("Direct State Attribute Example")

# Create the main button
button = tk.Button(root, text="Click Me!", state=tk.NORMAL, command=disable_button)
button.pack(pady=20)

# Create the button to enable the main button
enable_btn = tk.Button(root, text="Enable Button", command=enable_button)
enable_btn.pack(pady=20)

# Run the application
root.mainloop()
