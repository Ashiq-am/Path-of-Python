import wx

class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		fileMenu = wx.Menu()
		fileItem = fileMenu.Append(21, 'Menu Item1', 'Item 1')
		fileItem1 = fileMenu.Append(22, 'Menu Item1', 'Item 1')
		fileItem2 = fileMenu.Append(23, 'Menu Item1', 'Item 1')

		self.toolbar = self.CreateToolBar()
		td = self.toolbar.AddTool(1, '', wx.Bitmap('menu.png'), kind = wx.ITEM_DROPDOWN)
		# set dropdown menu with tool id 1
		self.toolbar.SetDropdownMenu(id = 1, menu = fileMenu)
		self.toolbar.Realize()
		self.SetSize((350, 250))
		self.SetTitle('Menu tool')
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
