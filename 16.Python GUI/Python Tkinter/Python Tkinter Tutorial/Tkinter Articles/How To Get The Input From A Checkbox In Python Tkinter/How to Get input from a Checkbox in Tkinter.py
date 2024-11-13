# Importing tkinter
import tkinter as tk
# Function to get the value from the checkbutton on checking or unchecking it.
def choice():
    # Checkbutton is checked.
    if choiceNum.get()==1:
        result_label.config(text="You ordered for Pizza")
    else:  # When checkbutton is unchecked.
        result_label.config(text="You do not want PIZZA!")
# GUI
window = tk.Tk()
window.title("Geeksforgeeks")
window.geometry("300x200")
window.config(bg="green")
# variable to listen to checkbutton
choiceNum = tk.IntVar()
label1 = tk.Label(window,text="Want Pizza?",font=("Arial",13),
                  bg="green",fg="white")
label1.pack()
# Checkbutton
chkbtn = tk.Checkbutton(window,text="Click to Order",
                        command=choice,onvalue=1,
                        offvalue=0,variable=choiceNum)
chkbtn.pack()
# Label to display the result.
result_label = tk.Label(window,fg="white",bg="green",font=("Arial",15))
result_label.pack()
window.mainloop()
