import wx

APP_EXIT = 1


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)

		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl + Q')
		qmi.SetBitmap(wx.Bitmap('right.png'))
		fileMenu.Append(qmi)

		self.Bind(wx.EVT_MENU, self.OnQuit, id = APP_EXIT)

		menubar.Append(fileMenu, '&File')
		self.SetMenuBar(menubar)

		self.SetSize((350, 250))
		self.SetTitle('Icons and shortcuts')
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
