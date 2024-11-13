def clickok():
    con = sqlite3.connect('studentrecords.db')
    c = con.cursor()
    num = int(e.get())
    try:
        c.execute(f'DELETE FROM StudentData WHERE Roll={num}')
        con.commit()
        Label(deletewin, fg="red", text="Deleted Successfully", font=("Helvetica", 10)).place(x=6, y=115)
    finally:
        deletewin.after(3000, lambda: deletewin.destroy())

def recdelete():
    global deletewin
    deletewin = Toplevel(root)
    global e
    e = Entry(deletewin, font=("Helvetica", 12))
    e.place(x=5, y=40)
    Label(deletewin, font=("Helvetica", 12), text="Please Enter Roll No",
          fg="purple").place(x=5, y=10)
    Button(deletewin, text="OK", command=lambda: clickok(), font=("Helvetica", 10),
           bg="lightpink", fg="purple", borderwidth=0).place(x=100, y=150)

def yesclk():
    con = sqlite3.connect('studentrecords.db')
    c = con.cursor()
    c.execute("DELETE FROM StudentData")
    con.commit()
    con.close()
    newwind.destroy()

def clearall():
    global newwind
    newwind = Toplevel(root)
    newwind.geometry('200x200')
    Button(newwind, font=("Helvetica", 12), text="Yes", borderwidth=0, bg="lightpink",
           fg="purple", command=yesclk).place(x=7, y=160)
    Button(newwind, font=("Helvetica", 12), text="No", borderwidth=0, bg="lightpink",
           fg="purple", command=lambda: newwind.destroy()).place(x=160, y=160)
    Label(newwind, font=("Arial", 15), text="Are You Sure?", fg="purple").place(x=15, y=25)
