from tkinter import *
from tkinter import messagebox

top = Tk()


def helpfile(filetype):
    if filetype == 1:
        with open("read.txt") as f:
            # reading file
            readme = f.read()

            # Display whole message
            messagebox.showinfo(title="Title",
                                message=str(readme))

        # Driver code


helpfile(1)
top.mainloop()
