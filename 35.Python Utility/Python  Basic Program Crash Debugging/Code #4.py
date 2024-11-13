import traceback
import sys

try:
	func(arg)
except:
	print('**** AN ERROR OCCURRED ****')
	traceback.print_exc(file = sys.stderr)
