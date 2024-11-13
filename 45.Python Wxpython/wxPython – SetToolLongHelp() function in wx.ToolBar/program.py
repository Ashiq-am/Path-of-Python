import wx

class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.toolbar = self.CreateToolBar()

		td = self.toolbar.AddTool(1, 'right', wx.Bitmap('right.png'))
		# set disabled bitmap for tool wit id = 1
		self.toolbar.SetToolDisabledBitmap(id = 1, bitmap = wx.Bitmap('wrong.png'))
		self.toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.OnOne, td)

		self.SetSize((350, 250))
		self.SetTitle('Undo redo')
		self.Centre()

	def OnOne(self, e):
		# set long help string for tool
		self.toolbar.SetToolLongHelp(toolId = 1, helpString ="This is new Long Help String.")
		str = self.toolbar.GetToolLongHelp(toolId = 1)
		print(str)
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
