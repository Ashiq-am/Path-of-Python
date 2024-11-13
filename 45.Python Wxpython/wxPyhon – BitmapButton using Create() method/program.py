import wx

class Mywin(wx.Frame):

	def __init__(self, parent, title):
		super(Mywin, self).__init__(parent, title = title, size =(250, 150))
		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.panel = wx.Panel(self)
		self.btn = wx.BitmapButton()
		bmp = wx.Bitmap('right.png')

		# CREATE BITMAPBUTTON USING Create() function
		self.btn.Create(self.panel, id = wx.ID_ANY, bitmap = bmp,
						size =(bmp.GetWidth()+10, bmp.GetHeight()+10))

		self.SetMinSize((400, 250))
		self.Centre()
		self.Show(True)



ex = wx.App()
Mywin(None, 'Window')
ex.MainLoop()
