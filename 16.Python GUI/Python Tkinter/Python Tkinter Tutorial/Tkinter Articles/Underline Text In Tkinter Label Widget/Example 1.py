import tkinter as tk
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("Underline Text in Tkinter Label")

# Create an underlined font
underlined_font = font.Font(family="Helvetica", size=12, underline=True)

# Create a Label widget with underlined text
label = tk.Label(root, text="This text is underlined", font=underlined_font)
label.pack(pady=20)

# Run the application
root.mainloop()
