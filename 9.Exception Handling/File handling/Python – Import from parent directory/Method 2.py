import path
import sys

# directory reach
directory = path.path(__file__).abspath()

# setting path
sys.path.append(directory.parent.parent)

# importing
from parentdirectory.geeks import geek_method

# using
geek_method()
