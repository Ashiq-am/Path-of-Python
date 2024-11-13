from matplotlib import pyplot as plt

Figure = plt.figure()

# creating a plot
lines_plotted = plt.plot([])

# putting limits on x axis since
# it is a trigonometry function
# (0,2∏)
line_plotted = lines_plotted[0]

plt.xlim(0,2*np.pi)

# putting limits on y since it is a
# cosine function
plt.ylim(-1.1,1.1)

# initialising x from 0 to 2∏
x = np.linspace(0,2*np.pi,100)

#initially
y = 0
