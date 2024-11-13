# importing the module
import os

# setting the path of the IDE
# use of \\ is important because
# \ will be treated as a escape sequence
# here we are using the Arduino Ide
# path to open the arduino ide
path="C:\\Program Files (x86)\\Arduino\\arduino.exe"

# using the os.startfile() method
os.startfile(path)
