import wx

class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.toolbar = self.CreateToolBar()
		td = self.toolbar.AddTool(1, 'right', wx.Bitmap('right.png'))
		self.toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.OnOne, td)

		self.SetSize((350, 250))
		self.SetTitle('Undo redo')
		self.Centre()

	def OnOne(self, e):
		# INSERT A DROPDOWN TOOL IN TOOLBAR
		self.toolbar.InsertTool(pos = 1, toolId = 2, label ='new', bitmap = wx.Bitmap('menu.png'), kind = wx.ITEM_DROPDOWN)
		# MENU TO BE ADDED TO TOOL
		fileMenu = wx.Menu()
		fileItem = fileMenu.Append(21, 'Menu Item1', 'Item 1')
		fileItem1 = fileMenu.Append(22, 'Menu Item1', 'Item 1')
		fileItem2 = fileMenu.Append(23, 'Menu Item1', 'Item 1')
		# SET DROPDOWN MENU
		self.toolbar.SetDropdownMenu(id = 2, menu = fileMenu)
		# Realize() called to finalize new added tools
		self.toolbar.Realize()

	def OnQuit(self, e):

		self.Close()


def main():

	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
