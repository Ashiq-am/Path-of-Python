# Importing Tkinter
import tkinter as tk
# GUI
root = tk.Tk()
root.title("GFG")
root.geometry("400x200")
# Convert image to PhotoImage variable.
gfg_picture = tk.PhotoImage(file="geeksforgeeks-logo.png")
# Frame created.
frame1 = tk.Frame(root, width=300, height=150)
frame1.pack()
# Label within the frame containing the image.
label1 = tk.Label(frame1, image=gfg_picture)
label1.pack()
root.mainloop()
