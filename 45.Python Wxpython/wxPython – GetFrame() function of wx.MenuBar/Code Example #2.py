import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()

		self.item = wx.MenuItem(self.fileMenu, 1, '&Check',
								helpString ="Check Help")
		self.item.SetBitmap(wx.Bitmap('right.png'))

		# SET BLUE COLOUR FOR TEXT FORMAT(R, B, G, A)
		self.item.SetTextColour((79, 81, 230, 255))
		self.fileMenu.Append(self.item)
		self.menubar.Append(self.fileMenu, '&File')
		self.SetMenuBar(self.menubar)
		self.SetSize((350, 250))

		# GET wx.Frame OBJECT
		frame = self.menubar.GetFrame()
		# SET NEW TITLE FOR FRAME
		frame.SetTitle('New Frame Title')
		self.Centre()

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
