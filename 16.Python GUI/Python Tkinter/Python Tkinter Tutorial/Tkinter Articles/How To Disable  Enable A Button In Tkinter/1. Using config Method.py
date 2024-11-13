import tkinter as tk

def disable_button():
    button.config(state=tk.DISABLED)

def enable_button():
    button.config(state=tk.NORMAL)

# Create the main window
root = tk.Tk()
root.title("Config Method Example")

# Create the main button
button = tk.Button(root, text="Click Me!", command=disable_button)
button.pack(pady=20)

# Create the button to enable the main button
enable_btn = tk.Button(root, text="Enable Button", command=enable_button)
enable_btn.pack(pady=20)

# Run the application
root.mainloop()
