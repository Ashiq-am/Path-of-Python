def clicksubmit():
    con = sqlite3.connect('studentrecords.db')
    c = con.cursor()

    studentname = name.get()
    rollnum = rollno.get()
    math_marks = maths.get()
    phy_marks = physics.get()
    chem_marks = chemistry.get()
    gender = "Male" if var.get() == 1 else "Female"

    c.execute("""INSERT INTO StudentData(Name, Roll, Gender, Maths, Physics, Chemistry) VALUES(?,?,?,?,?,?)""",
              (studentname, rollnum, gender, math_marks, phy_marks, chem_marks))

    con.commit()
    con.close()

    name.delete(0, END)
    rollno.delete(0, END)
    maths.delete(0, END)
    physics.delete(0, END)
    chemistry.delete(0, END)
