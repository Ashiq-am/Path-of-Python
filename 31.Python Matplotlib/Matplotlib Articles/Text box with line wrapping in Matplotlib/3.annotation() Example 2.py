import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
t = ("Welcome to GeeksforGeeks")
plt.text(5, 8, t, fontsize=18, style='oblique', ha='center',
		va='top', wrap=True)

plt.show()
