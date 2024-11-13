import wx

class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.toolbar = self.CreateToolBar()
		td = self.toolbar.AddTool(1, '', wx.Bitmap('sep.png'))
		te = self.toolbar.AddTool(2, '', wx.Bitmap('wrong.png'))
		tf = self.toolbar.AddTool(3, '', wx.Bitmap('right.png'))

		self.toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.OnOne, td)

		self.SetSize((350, 250))
		self.SetTitle('Undo redo')
		self.Centre()

	def OnOne(self, e):
		# insert stretchable space b / w separate
		# and tick tool at position 1
		self.toolbar.InsertStretchableSpace(pos = 1)
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
