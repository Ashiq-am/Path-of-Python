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
		self.toolbar.SetMargins(10, 10)
		# Add Tools Using AddTool function
		rtool = self.toolbar.AddTool(13, 'Toolone', wx.Bitmap('wrong.png'), shortHelp ="Simple Tool2")
		stool = self.toolbar.AddTool(14, 'Tooltwo', wx.Bitmap('wrong.png'), shortHelp ="Simple Tool")
		self.toolbar.Realize()
		self.toolbar.EnableTool(14, False)
		self.SetSize((350, 250))
		self.SetTitle('Control')
		self.Centre()

		bl = self.toolbar.GetToolEnabled(14)

		# print True of enabled
		print(bl)


def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
