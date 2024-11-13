import wx

class Mywin(wx.Frame):

	def __init__(self, parent, title):
		super(Mywin, self).__init__(parent, title = title, size =(250, 150))
		self.InitUI()

	def InitUI(self):
		self.panel = wx.Panel(self)
		self.btn = wx.Button(self.panel, label ="Click", pos =(75, 10))
		self.btn.Bind(wx.EVT_BUTTON, self.Onclick)

		self.SetMinSize((400, 250))
		self.Centre()
		self.Show(True)

	def Onclick(self, event):
		# SET A STRING LABEL FOR BUTTON
		self.btn.SetLabel("Clicked")


ex = wx.App()
Mywin(None, 'Window')
ex.MainLoop()
