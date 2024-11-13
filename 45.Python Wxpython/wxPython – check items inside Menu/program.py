import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		menubar = wx.MenuBar()
		viewMenu = wx.Menu()

		self.showsb = viewMenu.Append(wx.ID_ANY, 'Show statusbar',
												'Show Statusbar',
											kind = wx.ITEM_CHECK)

		viewMenu.Check(self.showsb.GetId(), True)

		self.Bind(wx.EVT_MENU, self.shStatusBar, self.showsb)

		menubar.Append(viewMenu, '&View')
		self.SetMenuBar(menubar)

		self.statusbar = self.CreateStatusBar()
		self.statusbar.SetStatusText('This is statusbar')

		self.SetSize((450, 350))
		self.SetTitle('Check menu item')
		self.Centre()


	def shStatusBar(self, e):

		if self.showsb.IsChecked():
			self.statusbar.Show()
		else:
			self.statusbar.Hide()

def main():

	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
