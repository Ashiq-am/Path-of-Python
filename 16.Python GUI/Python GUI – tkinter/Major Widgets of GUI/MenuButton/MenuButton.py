from tkinter import *

top = Tk()
top.geometry("200x250")
mb = Menubutton ( top, text = "ASHIQ", relief = RAISED)
mb.grid()
mb.menu = Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton ( label ='Decent', variable = cVar )
mb.menu.add_checkbutton ( label = 'Honest', variable = aVar )
mb.pack()
top.mainloop()

