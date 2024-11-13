import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.pnl = wx.Panel(self)


		# CREATE BUTTON AT POINT (20, 20)
		self.st = wx.Button(self.pnl, id = 1, label ="Button", pos =(20, 20),
								size = wx.DefaultSize, name ="button")
		# CREATE CURSOR OBJECT
		c = wx.Cursor(wx.Image('pointer.png'))
		# SET c AS CURSOR
		self.st.SetCursor(c)
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
