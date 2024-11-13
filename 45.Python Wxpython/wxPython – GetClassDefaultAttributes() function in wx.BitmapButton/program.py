import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		self.pnl = wx.Panel(self)
		bmp = wx.Bitmap('right.png')
		self.btn = wx.BitmapButton(self.panel, id = wx.ID_ANY, bitmap = bmp,
						size =(bmp.GetWidth()+10, bmp.GetHeight()+10))

		# wx.VisualAttributes OBJECT
		va = self.btn.GetClassDefaultAttributes(variant = wx.WINDOW_VARIANT_NORMAL)

		# PRINT PROPERTIES
		print(va.colBg)
		print(va.colFg)
		print(va.font)

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
