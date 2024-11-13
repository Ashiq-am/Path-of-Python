import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)

		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.item = wx.MenuItem(self.fileMenu, 1, '&Check', helpString ="Check Help", kind = wx.ITEM_CHECK)
		self.item.SetBitmap(wx.Bitmap('right.png'))
		self.item.SetTextColour((79, 81, 230, 255))
		self.item.Enable(True)
		self.st = wx.StaticText(self, label ="", pos =(200, 200))
		self.fileMenu.Append(self.item)
		self.menubar.Append(self.fileMenu, '&File')
		self.SetMenuBar(self.menubar)

		if self.item.IsEnabled()== True:
			# print if item is enable
			print("Item is Enabled")
		else:
			# print if item is disabled
			print("Item is Disabled")

		self.SetSize((350, 250))
		self.SetTitle('Icons and shortcuts')
		self.Centre()



def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
