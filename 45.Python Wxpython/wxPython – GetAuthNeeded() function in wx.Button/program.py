import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		self.pnl = wx.Panel(self)
		self.btn = wx.Button(self.pnl, label ='Button', pos =(20, 20))
		self.btn.SetAuthNeeded(True)

		# PRINT IF AUTHENTICATION IS NEEDED OR NOT USING GetAuthNeeded()
		if(self.btn.GetAuthNeeded()== True):
			print("Authentication is needed.")
		else:
			print("No Authentication is needed.")
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
