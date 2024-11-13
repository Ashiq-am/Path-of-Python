import scipy


# find method looks up in the dictorary and
# finds out all the constants containing
# 'electron' word in it and returns a list
# of constants.
res = scipy.constants.find("electron")
print(res, end='\n')
