# import numpy and stringIO
import numpy as np
from io import StringIO

buf = StringIO()
# using np.disp() method
np.disp(u'Geeks For Geeks', device = buf)
buf.getvalue()
