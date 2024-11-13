import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.pnl = wx.Panel(self)
		bmp = wx.Bitmap('right.png')
		# CREATE STATICTEXT AT POINT (20, 20)
		self.st = wx.StaticText(self.pnl, id = 1, label ="This is StaticText", pos =(20, 20),
								size = wx.DefaultSize, style = 0, name ="statictext")

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
