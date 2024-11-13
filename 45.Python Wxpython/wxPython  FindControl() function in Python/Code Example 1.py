import wx


class Example(wx.Frame):
	global count
	count = 0;

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		pnl = wx.Panel(self)
		self.toolbar = self.CreateToolBar()
		ctrl = wx.Control(self.toolbar, 21, wx.DefaultPosition, wx.DefaultSize, style = 0, name ='control')
		# Add control using AddControl() method
		rtool = self.toolbar.AddControl(ctrl, 'control')
		self.toolbar.Realize()
		self.SetSize((350, 250))
		self.SetTitle('Simple toolbar')
		self.Centre()

		print(self.toolbar.FindControl(21))

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
