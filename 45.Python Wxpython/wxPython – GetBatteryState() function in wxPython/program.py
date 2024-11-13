import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		# print battery state
		# 0 for wx.BATTERY_NORMAL_STATE
		# 1 for wx.BATTERY_LOW_STATE
		# 2 for wx.BATTERY_CRITICAL_STATE
		# 3 for wx.BATTERY_SHUTDOWN_STATE
		# 4 for wx.BATTERY_UNKNOWN_STATE
		print(wx.GetBatteryState())

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
