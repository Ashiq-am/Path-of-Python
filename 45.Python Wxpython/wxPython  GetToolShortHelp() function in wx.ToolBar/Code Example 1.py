import wx


class Example(wx.Frame):
	global count
	count = 0;

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		pnl = wx.Panel(self)
		self.toolbar = self.CreateToolBar()
		# Add Tools Using AddTool function
		rtool = self.toolbar.AddLabelTool(13, 'oneTool', wx.Bitmap('wrong.png'), shortHelp ="short help string one")
		stool = self.toolbar.AddLabelTool(14, 'twoTool', wx.Bitmap('user.png'), shortHelp ="short help string two")

		self.toolbar.Realize()
		self.SetSize((350, 250))
		self.SetTitle('Control')
		self.Centre()

		str = self.toolbar.GetToolShortHelp(13)

		# print wx.ToolBarToolBase object o tool
		print(str)


def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
