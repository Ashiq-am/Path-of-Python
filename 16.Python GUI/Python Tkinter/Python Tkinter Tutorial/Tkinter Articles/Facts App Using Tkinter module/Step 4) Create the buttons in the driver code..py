# driver code
from IPython.terminal.pt_inputhooks import tk

root = tk.Tk()

# adjust window
root.config(bg="red")
root.geometry("400x400")

# add buttons
button = tk.Button(root, text="Click here for Facts", command=move)
button2 = tk.Button(root, text="Clear and quit", command=destroy)
button.pack()
button2.pack()

root.mainloop()
