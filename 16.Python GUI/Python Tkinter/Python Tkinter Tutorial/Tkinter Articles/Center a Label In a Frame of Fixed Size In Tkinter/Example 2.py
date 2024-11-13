import tkinter as tk
# GUI
root = tk.Tk()
root.title("GFG")
root.geometry("500x500")
# Frame of fixed size
frame1 = tk.Frame(root, width=500, height=500)
frame1.grid(row=0, column=0)
# Label within the frame placed at center
label1 = tk.Label(frame1, text="Welcome to GeeksforGeeks",
                  fg="green", font=("Arial", 12, "bold"))
# The width of the frame created here is 500. So, on dividing it by 2, it is 250.
label1.place(x=250, y=250, anchor=tk.CENTER)
root.mainloop()
