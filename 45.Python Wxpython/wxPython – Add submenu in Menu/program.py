import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		menubar = wx.MenuBar()
		fileMenu = wx.Menu()

		# submenu for menuitem
		imp = wx.Menu()
		imp.Append(wx.ID_ANY, 'SubMenu 1')
		imp.Append(wx.ID_ANY, 'SubMenu 2')
		imp.Append(wx.ID_ANY, 'SubMenu 3')

		# append submenu with menuitem
		fileMenu.AppendMenu(wx.ID_ANY, 'MenuItem', imp)
		menubar.Append(fileMenu, '&Menu')
		self.SetMenuBar(menubar)

		self.SetSize((350, 250))
		self.SetTitle('Submenu')
		self.Centre()

	def OnQuit(self, e):
		self.Close()


def main():

	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
