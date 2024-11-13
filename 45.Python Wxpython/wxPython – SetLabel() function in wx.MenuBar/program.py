import self as self
import wx
from Demos.SystemParametersInfo import w


class Example(wx.Frame):
	super(w).__init__(*args, **kwargs)

	# create MenuBar using MenuBar() function
	menubar = wx.MenuBar()

	# add menu to MenuBar
	fm1 = wx.Menu()
	fileitem = fm1.Append(20, "Item # 1")
	menubar.Append(fm1, '&Menu # 1')
	self.SetMenuBar(menubar)
	self.SetSize((300, 200))
	self.SetTitle('Menu Bar')

	# change label of menu item to New Name
	menubar.SetLabel(20, "New Name")


def main():

	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
