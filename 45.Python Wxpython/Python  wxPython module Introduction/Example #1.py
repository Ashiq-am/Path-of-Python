# import wx module
import wx

# creaing application object
app1 = wx.App()

# creating a frame
frame = wx.Frame(None, title ="GFG")
pa = wx.Panel(frame)

# Adding a text to the frame object
text1 = wx.StaticText(pa, label ="GEEKS FOR GEEKS", pos =(100, 50))

# show it
frame.Show()

# start the event loop
app1.Mainloop()
