# import wxPython
import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		# create MenuBar using MenuBar() function
		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		# add menu to MenuBar
		menubar.Append(fileMenu, '&Menu# 1')
		self.SetMenuBar(menubar)

		self.SetSize((300, 200))
		self.SetTitle('Menu Bar')
def main():

	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
