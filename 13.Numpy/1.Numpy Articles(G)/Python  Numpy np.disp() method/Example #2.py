# import numpy and stringIO
import numpy as np
from io import StringIO

buf = StringIO()
# using np.disp() method
np.disp(u'Author "Jitender Kumar"', device = buf)
buf.getvalue()
