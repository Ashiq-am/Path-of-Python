import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		self.pnl = wx.Panel(self)
		self.btn = wx.Button(self.pnl, label ='Button',
							pos =(20, 20), size =(100, 20))

		# GET DEFAULT SIZE
		s = self.btn.GetDefaultSize(self)
		# PRINT DEFAULT SIZE
		print(s)

		self.SetSize((350, 250))
		self.SetTitle('wx.Button')
		self.Centre()

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
