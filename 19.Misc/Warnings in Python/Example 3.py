# program to illustrate filterwarnings()
# function in warning module

# importing module
import warnings

# adding entry into the specifications
# of the warnings filter.
warnings.filterwarnings('ignore', '.*do not.*', )

# displaying warinings
warnings.warn('Geeks 4 Geeks !')

# this warning will not be displayed
warnings.warn('Do not show this message')
