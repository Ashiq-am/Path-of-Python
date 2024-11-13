import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		pnl = wx.Panel(self)
		self.toolbar = self.CreateToolBar()
		qtool = self.toolbar.AddTool(12, 'Quit', wx.Bitmap('/Desktop/wxPython/signs.png'))
		self.toolbar.Realize()

		self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

		self.SetSize((350, 250))
		self.SetTitle('Simple toolbar')
		self.Centre()
		self.btn = wx.Button(pnl, label ='Disable', pos =(20, 20))

		self.btn.Bind(wx.EVT_BUTTON, self.Onclick)

		self.SetSize((350, 250))
		self.SetTitle('wx.Button')
		self.Centre()


	def OnQuit(self, e):
		self.Close()

	def Onclick(self, e):
		# disable tool using EnableTool
		self.toolbar.EnableTool(12, False)


def main():

	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
