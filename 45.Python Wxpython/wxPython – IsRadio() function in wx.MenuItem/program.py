import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)

		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.item = wx.MenuItem(self.fileMenu, 1, '&Radio 1', helpString ="Check Help", kind = wx.ITEM_RADIO)
		self.item2 = wx.MenuItem(self.fileMenu, 1, '&Radio 2', helpString ="Check Help", kind = wx.ITEM_RADIO)
		self.item.SetTextColour((79, 81, 230, 255))
		self.item2.SetTextColour((79, 81, 230, 255))
		self.st = wx.StaticText(self, label ="", pos =(200, 200))
		self.fileMenu.Append(self.item)
		self.fileMenu.Append(self.item2)
		self.menubar.Append(self.fileMenu, '&File')
		self.SetMenuBar(self.menubar)

		if self.item.IsRadio()== True:
			# print if item is radio
			print("Item is Radio")
		else:
			# print if item is not radio
			print("Item is not Radio")

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
