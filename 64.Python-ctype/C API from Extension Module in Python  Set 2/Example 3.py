# setup.py
from distutils.core import setup, Extension

# May need pythonsample.h directory
setup(name ='ptexample',
	ext_modules = [ Extension('ptexample',
					['ptexample.c'], include_dirs = [], )])
