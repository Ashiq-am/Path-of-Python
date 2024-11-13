import matplotlib.pyplot as plt

x =['Geeks', 'for', 'geeks', 'tutorials']
y =[1, 2, 3, 4]

# Setting font dictionary
font = {'family': 'Verdana',
		'color': 'green',
		'size': 20,
		}

# Adding the font styles to the label
plt.ylabel('Numbers label', fontdict = font)

plt.plot(x, y)
