# import wxPython
import wx


class Example(wx.Frame):

	def __init__(self, *args, **kw):
		super(Example, self).__init__(*args, **kw)

		self.InitUI()

	def InitUI(self):

		pnl = wx.Panel(self)
		Button = wx.Button(pnl, label ='New Frame', pos =(20, 20))

		Button.Bind(wx.EVT_BUTTON, self.OnNewFrame)

		self.SetSize((350, 250))
		self.SetTitle('wx.Button')

	def OnNewFrame(self, e):
		app = wx.App()
		frm = wx.Frame()
		frm.Create(None, title ="Frame using Create()")
		frm.Show()
		app.MainLoop()

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
