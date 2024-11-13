import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		# create MenuBar using MenuBar() function
		menubar = wx.MenuBar()

		# menu for menuitem
		fm1 = wx.Menu()
		fm2 = wx.Menu()
		fm3 = wx.Menu()

		menubar.Append(fm1, '&Menu# 1')
		menubar.Append(fm2, '&Menu# 2')
		menubar.Append(fm3, '&Menu# 3')

		self.SetMenuBar(menubar)
		self.SetSize((300, 200))
		self.SetTitle('Menu Bar')

		# get index of menuitem using FindMenu function
		index = menubar.FindMenu("&Menu# 3")
		print(index)

def main():

	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
