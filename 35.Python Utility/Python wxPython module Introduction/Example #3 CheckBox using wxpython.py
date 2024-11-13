# importing wx module
import wx

# creaing application object
app1 = wx.App()

# creating a frame
frame = wx.Frame(None, title ="wxpython app")
pa = wx.Panel(frame)

# Checkbox creation using wx module
e = wx.CheckBox(pa, -1, "CheckBox1", pos = (120, 100))
e = wx.CheckBox(pa, -1, "CheckBox2", pos = (120, 120))

# show it
frame.Show()

# start the event loop
app1.Mainloop()
