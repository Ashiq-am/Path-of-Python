import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		# CREATE MENU
		self.submenu = wx.Menu()
		self.submenu.Append(wx.ID_ANY, 'ONE')
		self.submenu.Append(wx.ID_ANY, 'TWO')
		self.submenu.Append(wx.ID_ANY, 'THREE')
		self.st = wx.StaticText(self, label ="", pos =(20, 20),
										style = wx.ALIGN_LEFT)
		self.item = wx.MenuItem(None, 1, '&Radio', kind = wx.ITEM_CHECK)

		# SET self.submenu AS SUBMENU FOR self.item MENUITEM
		self.item.SetSubMenu(self.submenu)
		self.fileMenu.Append(self.item)
		self.menubar.Append(self.fileMenu, '&File')
		self.SetMenuBar(self.menubar)
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
