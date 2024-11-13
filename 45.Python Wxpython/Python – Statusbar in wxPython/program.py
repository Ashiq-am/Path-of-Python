# import wxython
import wx


class Example(wx.Frame):

	def __init__(self, *args, **kw):
		super(Example, self).__init__(*args, **kw)
		self.InitUI()

	def InitUI(self):
		# create status bar
		self.statusBar = self.CreateStatusBar(style = wx.BORDER_NONE)
		# set text t status bar
		self.statusBar.SetStatusText("Status Bar")

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
