# importing tkinter
import tkinter as tk


# GUI
root = tk.Tk()
root.title("GeeksForGeeks")
root.geometry("280x100")
root.config(bg="green")
tk.Label(root, text="Welcome to GFG!", fg="white",
         bg="green", font=("Arial", 16, "bold")).pack(pady=15)
root.mainloop()
