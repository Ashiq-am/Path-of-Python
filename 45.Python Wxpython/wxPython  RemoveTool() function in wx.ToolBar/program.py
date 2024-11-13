import wx

class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.toolbar = self.CreateToolBar()
		td = self.toolbar.AddTool(1, '', wx.Bitmap('wrong.png'))
		te = self.toolbar.AddTool(2, '', wx.Bitmap('right.png'))
		tf = self.toolbar.AddTool(3, '', wx.Bitmap('sep.png'))
		self.toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.OnOne, td)

		self.SetSize((350, 250))
		self.SetTitle('Undo redo')
		self.Centre()

	def OnOne(self, e):
		# delete tools from toolbar using RemoveTool() function
		self.toolbar.RemoveTool(id = 2)
		self.toolbar.RemoveTool(id = 3)
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
