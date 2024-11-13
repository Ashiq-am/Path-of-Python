# Importing tkinter
import tkinter as tk
# GUI
root = tk.Tk()
root.title("GFG")
root.geometry("300x300")
# Frame of fixed size
frame1 = tk.Frame(root, width=300, height=300)
frame1.grid(row=0, column=0)
# Label within the frame placed at center
label1 = tk.Label(frame1, text="Welcome to GeeksforGeeks",
                  fg="green", font=("Arial", 12, "bold"))
label1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
root.mainloop()
