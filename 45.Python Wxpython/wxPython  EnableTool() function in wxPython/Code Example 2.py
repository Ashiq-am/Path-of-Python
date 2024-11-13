import wx


class Example(wx.Frame):
	global count
	count = 0

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		pnl = wx.Panel(self)
		self.toolbar = self.CreateToolBar()
		# Add Tools Using AddTool function
		rtool = self.toolbar.AddTool(13, 'twoTool', wx.Bitmap('user.png'), shortHelp ="Simple Tool2")
		stool = self.toolbar.AddTool(14, 'twoTool', wx.Bitmap('right.png'), shortHelp ="Simple Tool2")

		self.toolbar.Realize()
		self.SetSize((350, 250))
		self.SetTitle('Control')
		self.Centre()

		# disable tool in toolbar
		self.toolbar.EnableTool(13, False)


def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
