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

		# Add tools to toolbar
		ptool = self.toolbar.AddTool(12, 'oneTool',
									wx.Bitmap('right.png'),
									wx.Bitmap('wrong.png'), shortHelp ="Simple Tool")

		qtool = self.toolbar.AddTool(12, 'oneTool', wx.Bitmap('wrong.png'),
									wx.Bitmap('wrong.png'), shortHelp ="Simple Tool")

		# change background colour of toolbar
		self.toolbar.SetBackgroundColour((255, 200, 50, 255))

		# print background colour of toolbar (r, g, b, a)
		print(self.toolbar.GetBackgroundColour())

		self.toolbar.Realize()
		self.SetSize((350, 250))
		self.SetTitle('Control')
		self.Centre()


def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
