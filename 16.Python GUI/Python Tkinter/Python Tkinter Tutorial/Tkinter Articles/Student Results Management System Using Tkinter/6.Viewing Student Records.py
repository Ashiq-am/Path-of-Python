def display_results(subject):
    newwind = Toplevel(root)
    Label(newwind, text="Name", font=("Helvetica", 10), fg="purple", bg="lightpink").place(x=2, y=0)
    Label(newwind, text="Roll Number", font=("Helvetica", 10), fg="purple", bg="lightpink").place(x=152, y=0)
    Label(newwind, text="Marks Obtained", font=("Helvetica", 10), fg="purple", bg="lightpink").place(x=302, y=0)
    newwind.geometry('400x400')

    con = sqlite3.connect('studentrecords.db')
    c = con.cursor()
    rows = c.execute(f"SELECT Name, Roll, {subject} FROM StudentData ORDER BY {subject} desc")

    y1 = 30
    for row in rows:
        s_name, roll, marks = row
        Label(newwind, font=("Helvetica", 10), fg="purple", bg="lightpink", text=s_name).place(x=2, y=y1)
        Label(newwind, font=("Helvetica", 10), fg="purple", bg="lightpink", text=str(roll)).place(x=152, y=y1)
        Label(newwind, font=("Helvetica", 10), fg="purple", bg="lightpink", text=str(marks)).place(x=302, y=y1)
        y1 += 30

Button(root, text="Display Maths Results", bg="purple", fg="white", font=("Helvetica", 15),
       command=lambda: display_results("Maths"), borderwidth=0).place(x=500, y=50)
Button(root, text="Display Physics Results", bg="purple", fg="white", font=("Helvetica", 15),
       command=lambda: display_results("Physics"), borderwidth=0).place(x=500, y=95)
Button(root, text="Display Chemistry Results", bg="purple", fg="white", font=("Helvetica", 15),
       command=lambda: display_results("Chemistry"), borderwidth=0).place(x=500, y=140)
