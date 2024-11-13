from inspect import getsourcefile

import os


print(os.path.dirname(getsourcefile(lambda:0)))
