import wx


class Example(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		pnl = wx.Panel(self)
		self.toolbar = self.CreateToolBar()
		# Add Tools Using AddTool function
		rtool = self.toolbar.AddLabelTool(id = 13, label = "Tool one", bitmap = wx.Bitmap('right.png'), shortHelp ="short help 1", longHelp = "Long help associated with simple tool 1")
		stool = self.toolbar.AddLabelTool(id = 14, label = "Tool two", bitmap = wx.Bitmap('wrong.png'), shortHelp ="short help 2", longHelp = "Long help associated with simple tool 2")

		self.toolbar.Realize()
		self.SetSize((350, 250))
		self.SetTitle('Control')
		self.Centre()
		# variable bl storing position of tool
		bl = self.toolbar.GetToolPos(13)

		# print tool position value
		print(bl)


def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
