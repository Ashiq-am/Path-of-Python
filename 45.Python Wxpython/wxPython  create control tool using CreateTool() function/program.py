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
		# declare control
		ctrl = wx.Control(self.toolbar, id = 19, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, name ='control')
		# create control tool
		self.ptool = self.toolbar.CreateTool(ctrl, "control")
		self.btn = wx.Button(pnl, label ='Add created tool', pos =(20, 20))

		self.btn.Bind(wx.EVT_BUTTON, self.Onclick)
		self.toolbar.Realize()
		self.SetSize((350, 250))
		self.SetTitle('Control')
		self.Centre()

	def Onclick(self, e):
		# Add control tool
		self.toolbar.AddTool(self.ptool)
		self.btn.SetLabel("Added tool")

def main():

	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
