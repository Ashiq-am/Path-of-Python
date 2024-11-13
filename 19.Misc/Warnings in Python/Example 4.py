# program to illustrate simplefilter()
# function in warning module

# importing module
import warnings

# adding a single entry into warnings filter
warnings.simplefilter('error', UserWarning)

# displaying the warning
warnings.warn('This is a warning message')
