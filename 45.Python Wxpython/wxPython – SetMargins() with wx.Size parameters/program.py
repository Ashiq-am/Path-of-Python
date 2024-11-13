import wx

class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.toolbar = self.CreateToolBar()
		# set margins with size parameter
		self.toolbar.SetMargins(size =(30, 25))
		td = self.toolbar.AddTool(1, 'right', wx.Bitmap('right.png'))
		self.toolbar.Realize()
		# print margins
		print(self.toolbar.GetMargins())
		self.SetSize((350, 250))
		self.SetTitle('Undo redo')
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
