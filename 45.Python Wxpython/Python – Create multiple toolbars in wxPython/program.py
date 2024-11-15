import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		vbox = wx.BoxSizer(wx.VERTICAL)

		toolbar1 = wx.ToolBar(self)
		toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('/Desktop/wxPython/signs.png'))
		toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('/Desktop/wxPython/login.png'))

		toolbar1.Realize()

		toolbar2 = wx.ToolBar(self)
		qtool = toolbar2.AddTool(wx.ID_EXIT, '', wx.Bitmap('/Desktop/wxPython/password.png'))
		toolbar2.Realize()

		vbox.Add(toolbar1, 0, wx.EXPAND)
		vbox.Add(toolbar2, 0, wx.EXPAND)

		self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

		self.SetSizer(vbox)

		self.SetSize((600, 4000))
		self.SetTitle('Multiple Toolbars')
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
