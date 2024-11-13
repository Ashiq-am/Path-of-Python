import wx

class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		self.count = 5
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.toolbar = self.CreateToolBar()
		tundo = self.toolbar.AddTool(wx.ID_UNDO, '', wx.Bitmap('right.png'))
		tredo = self.toolbar.AddTool(wx.ID_REDO, '', wx.Bitmap('wrong.png'))
		self.toolbar.EnableTool(wx.ID_REDO, False)
		self.toolbar.AddSeparator()
		self.toolbar.Realize()
		self.txt = wx.StaticText(self, 121, "Enabled")
		self.Bind(wx.EVT_TOOL, self.OnUndo, tundo)
		self.Bind(wx.EVT_TOOL, self.OnRedo, tredo)

		self.SetSize((350, 250))
		self.SetTitle('Undo redo')
		self.Centre()

	def OnUndo(self, e):
		if(self.toolbar.GetToolState(wx.ID_UNDO)== True):
			self.txt.SetLabel("Enabled")
		else:
			self.txt.SetLabel("Disabled")

		if self.count > 1 and self.count <= 5:
			self.count = self.count - 1

		if self.count == 1:
			self.toolbar.EnableTool(wx.ID_UNDO, False)

		if self.count == 4:
			self.toolbar.EnableTool(wx.ID_REDO, True)

	def OnRedo(self, e):
		if self.count < 5 and self.count >= 1:
			self.count = self.count + 1

		if self.count == 5:
			self.toolbar.EnableTool(wx.ID_REDO, False)

		if self.count == 2:
			self.toolbar.EnableTool(wx.ID_UNDO, True)


	def OnQuit(self, e):
		self.Close()


def main():

	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
