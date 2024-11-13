# Import wx module
import wx

# creaing application object
app1 = wx.App()

# creating a frame
frame = wx.Frame(None, title ="wxpython app")
pa = wx.Panel(frame)

# Button creation
e = wx.Button(pa, -1, "Button1", pos = (120, 100))

# show it
frame.Show()

# start the event loop
app1.Mainloop()
