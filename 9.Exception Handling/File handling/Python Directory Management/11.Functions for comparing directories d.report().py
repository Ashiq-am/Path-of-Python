import filecmp as fc
import os

dir_1 = dir_2 = os.getcwd()

# creating object and invoking constructor
d = fc.dircmp(dir_1, dir_2, ignore=None, hide=None)

print("comparison 1 :")
d.report()
