# importing libraries
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension('work',
						['work.pyx'],
						libraries=['work'],
						library_dirs=['.'])]

setup(name = 'work extension module',
	cmdclass = {'build_ext': build_ext},
	ext_modules = ext_modules)
