import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()


	def InitUI(self):
		# create MenuBar using MenuBar() function
		menubar = wx.MenuBar()

		# add menu to MenuBar
		fm1 = wx.Menu()
		fileitem = fm1.Append(20, "Item # 1")
		menubar.Append(fm1, '&Menu # 1')
		self.SetMenuBar(menubar)
		self.SetSize((300, 200))
		self.SetTitle('Menu Bar')

		# set helpstring using SetHelpString() function
		menubar.SetHelpString(20, "Help String")
		st = wx.StaticText(self, label ="click Item # 1 in Menu # 1")
		print(menubar.GetHelpString(20))

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
