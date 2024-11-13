import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.pnl = wx.Panel(self)

		# create wx.Font object
		font = wx.Font(20, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,
					underline = False, faceName ="", encoding = wx.FONTENCODING_DEFAULT)

		self.st = wx.StaticText(self.pnl, id = 1, label ="This is the Label.", pos =(20, 20),
								size = wx.DefaultSize, style = wx.ST_ELLIPSIZE_MIDDLE, name ="statictext")

		# set font for the statictext
		self.st.SetFont(font)

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
