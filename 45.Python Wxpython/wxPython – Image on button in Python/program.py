# import wxPython
import wx

# event function for button
def onButton(event):
	print("Button pressed.")

app = wx.App()
frame = wx.Frame(None, -1, 'win.py')
frame.SetDimensions(0, 0, 200, 70)
panel = wx.Panel(frame, wx.ID_ANY)

# open image from disk
bmp = wx.Bitmap("/home/rahul101/Desktop/wxPython/images.png", wx.BITMAP_TYPE_ANY)
# create image button using BitMapButton constructor
button = wx.BitmapButton(panel, id = wx.ID_ANY, bitmap = bmp,
						size =(bmp.GetWidth()+10, bmp.GetHeight()+10))

button.Bind(wx.EVT_BUTTON, onButton)
button.SetPosition((10, 10))

frame.Show()
frame.Centre()
app.MainLoop()
