import wx

class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.toolbar = self.CreateToolBar()
		tundo = self.toolbar.AddTool(1, '', wx.Bitmap('right.png'))
		tredo = self.toolbar.AddTool(2, '', wx.Bitmap('wrong.png'))

		self.toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.OnOne, tundo)

		self.SetSize((350, 250))
		self.SetTitle('Undo redo')
		self.Centre()

	def OnOne(self, e):
		ctrl = wx.Control(self.toolbar, id = 1, size =(100, -1),
		style = 0, name ="control")
		# insert control in toolbar at position 2
		self.toolbar.InsertControl(pos = 0, control = ctrl, label ="Control")
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
