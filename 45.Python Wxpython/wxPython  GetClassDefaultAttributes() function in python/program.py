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
		rtool = self.toolbar.AddTool(13, 'twoTool', wx.Bitmap('wrong.png'), shortHelp ="Simple Tool2")

		self.toolbar.Realize()
		self.SetSize((350, 250))
		self.SetTitle('Control')
		self.Centre()

		# get Visual attribute object
		t = self.toolbar.GetClassDefaultAttributes(variant = wx.WINDOW_VARIANT_NORMAL)
		# print background color ratio
		print(t.colBg)
		# print foreground color ratio
		print(t.colFg)
		# print wx.Font object
		print(t.font)

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
