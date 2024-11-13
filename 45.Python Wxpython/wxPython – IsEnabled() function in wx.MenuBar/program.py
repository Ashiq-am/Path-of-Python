import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fileMenu2 = wx.Menu()
		self.item = wx.MenuItem(self.fileMenu, 1, '&Check', helpString ="Check Help",
															kind = wx.ITEM_CHECK)
		self.item.SetBitmap(wx.Bitmap('right.png'))
		self.fileMenu.Append(self.item)

		# DISABLE MENU ITEM
		self.item.Enable(False)
		self.menubar.Append(self.fileMenu, '&File')
		self.SetMenuBar(self.menubar)
		self.SetSize((350, 250))
		self.SetTitle('New Frame Title')
		self.Centre()
		if(self.menubar.IsEnabled(1)== True):
			# print CLICKABLE if True
			print("CLICKABLE")
		else:
			# else print UNCLICKABLE
			print("UNCLICKABLE")

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
