import numpy as np
import matplotlib.pyplot as plt
import matplotlib.text as text

m = np.arange(3, -4, -.2)
n = np.arange(3, -4, -.2)
o = np.exp(m)
p = o[::-1]

figure, axes = plt.subplots()
plt.plot(m, o, 'k--', m, p,
		'k:', m, o + p, 'k')

plt.legend((' Modelset', 'Dataset',
			'Total string length'),
		loc ='upper center',
		shadow = True)
plt.ylim([-1, 10])
plt.grid(True)
plt.xlabel(' Modelset --->')
plt.ylabel(' String length --->')
plt.title('Min. Length of String')


# Helper function
def find_match(x):
	return hasattr(x, 'set_color') and not hasattr(x, 'set_facecolor')

# calling the findobj function
for obj in figure.findobj(find_match):
	obj.set_color('black')

# match on class instances
for obj in figure.findobj(text.Text):
	obj.set_fontstyle('italic')


plt.show()
