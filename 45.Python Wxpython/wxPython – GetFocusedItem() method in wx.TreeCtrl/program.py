# import required modules
import wx


class MyTree(wx.TreeCtrl):

	def __init__(self, parent, id, pos, size, style):
		wx.TreeCtrl.__init__(self, parent, id, pos, size, style)


class TreePanel(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

	# create tree control in window
		self.tree = MyTree(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
						wx.TR_HAS_BUTTONS)

		# create tree root
		self.root = self.tree.AddRoot('root')
		self.tree.SetPyData(self.root, ('key', 'value'))

		# add item to root
		item = self.tree.AppendItem(self.root, "Item")
		item2 = self.tree.AppendItem(self.root, "Item")

		# set focused/selected item in control
		self.tree.SetFocusedItem(item)

		# print if first visible item is
		# a valid tree item
		if(self.tree.GetFocusedItem().IsOk()):
			print("Valid Item")
			print(self.tree.GetFocusedItem())
		else:
			print("Invalid Item")

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.tree, 100, wx.EXPAND)
		self.SetSizer(sizer)


class MainFrame(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self, parent=None, title='TreeCtrl Demo')
		panel = TreePanel(self)
		self.Show()


# Driver Code
if __name__ == '__main__':
	app = wx.App(redirect=False)
	frame = MainFrame()
	app.MainLoop()
