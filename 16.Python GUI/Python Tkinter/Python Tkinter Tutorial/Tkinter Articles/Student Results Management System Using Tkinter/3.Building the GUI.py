root = Tk()
root.geometry('1000x500')
root.title('Exam Records')
var = IntVar()

# Creating Labels
Label(root, font=("Arial", 15), fg="purple", text="Exam Records").place(x=210, y=30)
Label(root, font=("Helvetica", 12), fg="purple", text="Name").place(x=69, y=120)
Label(root, font=("Helvetica", 12), fg="purple", text="Gender").place(x=69, y=164)
Label(root, font=("Helvetica", 12), fg="purple", text="Roll Number").place(x=69, y=208)
Label(root, font=("Helvetica", 12), fg="purple", text="Mathematics").place(x=69, y=250)
Label(root, font=("Helvetica", 12), fg="purple", text="Physics").place(x=69, y=290)
Label(root, font=("Helvetica", 12), text="Chemistry", fg="purple").place(x=69, y=330)

# Creating Entry Boxes
name = Entry(root, font=("Helvetica", 12), width=27, bg="lightblue")
rbutton1 = Radiobutton(root, font=("Helvetica", 12), fg="red", variable=var, value=1, text="Male")
rbutton2 = Radiobutton(root, font=("Helvetica", 12), fg="green", variable=var, value=2, text="Female")
rollno = Entry(root, font=("Helvetica", 12), width=27, bg="lightblue")
maths = Entry(root, font=("Helvetica", 12), width=27, bg="lightblue")
physics = Entry(root, font=("Helvetica", 12), width=27, bg="lightblue")
chemistry = Entry(root, font=("Helvetica", 12), width=27, bg="lightblue")

# Placing Widgets
name.place(x=170, y=122)
rbutton1.place(x=170, y=164)
rbutton2.place(x=250, y=164)
rollno.place(x=170, y=207)
maths.place(x=170, y=249)
physics.place(x=170, y=289)
chemistry.place(x=170, y=329)

# Create Buttons
Button(root, font=("Arial", 15), fg="white", bg="purple", text="Submit", borderwidth=0, command=lambda: clicksubmit()).place(x=242, y=369)
Button(root, font=("Helvetica", 12), bg="green", fg="white", text="Delete A Record", borderwidth=0, command=recdelete).place(x=220, y=410)
Button(root, font=("Helvetica", 12), text="Clear Database", bg="red", fg="white", borderwidth=0, command=clearall).place(x=223, y=450)
