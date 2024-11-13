import wx


class Example(wx.Frame):
	global count
	count = 0

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.toolbar = self.CreateToolBar()
		tool = self.toolbar.AddTool(wx.ID_ANY, 'First',
								wx.Bitmap('right.png'))
		self.toolbar.Realize()

		# panel for button
		self.pnl = wx.Panel(self)

		# button to hide toolbar
		self.btn = wx.Button(self.pnl, label ='Hide Toolbar', pos =(20, 20))

		# button to show toolbar
		self.btn2 = wx.Button(self.pnl, label ='Show Toolbar', pos =(200, 20))

		# bind event with hide button
		self.btn.Bind(wx.EVT_BUTTON, self.onclickhide)

		# bind event with show button
		self.btn2.Bind(wx.EVT_BUTTON, self.onclickshow)

		self.SetSize((350, 250))
		self.SetTitle('Simple toolbar')
		self.Centre()

	def onclickhide(self, e):
		# hide toolbar
		self.toolbar.Hide()

	def onclickshow(self, e):
		# hide toolbar
		self.toolbar.Show(True)

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
