# import wxPython
import wx

# frame class
class MoveWindow(wx.Frame):

	def __init__(self, parent, title):
		super(MoveWindow, self).__init__(parent, title = title,
			size =(300, 200))
		# move window to (900, 600) using Move() function
		self.Move((900, 600))


def main():
	app = wx.App()
	move = MoveWindow(None, title ='Move()')
	move.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
