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

		# get id identifier of submenu item
		id = menubar.FindMenuItem("&Menu # 1", "Item # 1")
		print(id)

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
