# import deepcopy module
from copy import deepcopy

# create an empty list
l = []

# create a dictionary wih student details
student = {7058: 'sravan kumsr Gottumukkala',
		7059: 'ojaswi', 7060: 'bobby',
		7061: 'gnanesh', 7062: 'rohith'}

# append this dictionary to
# the empty list using deepcopy() method
l.append(deepcopy(student))

# display list
l
