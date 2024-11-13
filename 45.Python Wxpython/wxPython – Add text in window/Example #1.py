# import wxPython
import wx

# create base class
class TextExample(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(TextExample, self).__init__(*args, **kwargs)

		# lets put some text
		st = wx.StaticText(self, label ="Welcome to GeeksforGeeks")

def main():
	app = wx.PySimpleApp()
	frame = TextExample(None, title = "Read Text")
	frame.Show()
	app.MainLoop()

if __name__ == '__main__':
	main()
