import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

# creating button
btn = tk.Button(root, text ="I am button")
btn.pack()

# takefocus is set to 0 for disabling the TAB key
# focus in widget
btn_no_focus = tk.Button(root, text ="I am not focused",
						takefocus = 0,foreground = "red")
btn_no_focus.pack()

# created an entry widget with width 10
txt = tk.Entry(root, width = 10)
txt.pack()

# creating a entry widget with width 10 and focus is
# 0 hence disabled
txt = tk.Entry(root, width = 10, takefocus = 0)
txt.pack()

# Creating radiobutton
rb = tk.Radiobutton(root, text ="I am radio button")
rb.pack()

# putting an takefocus=0 for disabling focus
rb_unfocus = tk.Radiobutton(root, text ="I am unfocused radio button",
							takefocus = 0,foreground = "red")
rb_unfocus.pack()

# creating the checkbutton
cb = tk.Checkbutton(root, text = "I am check button")
cb.pack()


cb_unfocused = tk.Checkbutton(root, text = "I am unfocused check button",
							takefocus = 0, foreground = "red")
cb_unfocused.pack()

root.mainloop()
