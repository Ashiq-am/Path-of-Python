import wx

class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.toolbar = self.CreateToolBar()
		td = self.toolbar.AddTool(1, '', wx.Bitmap('user.png'))

		self.toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.OnOne, td)

		self.SetSize((350, 250))
		self.SetTitle('Undo redo')
		self.Centre()

	def OnOne(self, e):
		# insert tool at position 1
		self.toolbar.InsertLabelTool( pos = 1, id = 3, label ='new tool1', bitmap = wx.Bitmap('right.png'), kind = wx.ITEM_NORMAL, shortHelp ="nono")
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
