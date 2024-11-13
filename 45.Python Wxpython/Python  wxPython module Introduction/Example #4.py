# importing wx module
import wx

# creaing application object
app1 = wx.App()

# creating a frame
frame = wx.Frame(None, title ="wxpython app")
pa = wx.Panel(frame)

# RadioButton creation using wx module
e = wx.RadioButton(pa, -1, "RadioButton1", pos = (120, 100))
e = wx.RadioButton(pa, -1, "radioButton2", pos = (120, 120))

# show it
frame.Show()

# start the event loop
app1.Mainloop()
