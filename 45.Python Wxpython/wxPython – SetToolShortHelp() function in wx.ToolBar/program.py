import wx

class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.toolbar = self.CreateToolBar()

		td = self.toolbar.AddTool(1, 'right', wx.Bitmap('right.png'))
		te = self.toolbar.AddTool(2, 'wrong', wx.Bitmap('wrong.png'))

		# set separation of toolbar to 20
		self.toolbar.SetToolShortHelp(toolId = 1, helpString ="new short help")

		self.toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.OnOne, td)

		self.SetSize((350, 250))
		self.SetTitle('Undo redo')
		self.Centre()

	def OnOne(self, e):
		print(self.toolbar.GetToolSeparation())
		# Realize() called to finalize new added tools
		self.toolbar.Realize()

	def OnQuit(self, e):
		self.Close()


def main():

	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
