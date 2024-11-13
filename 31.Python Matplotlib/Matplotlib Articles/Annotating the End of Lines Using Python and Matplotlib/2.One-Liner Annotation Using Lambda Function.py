import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y)

# One-liner annotation
(lambda a, b: plt.annotate(f'{b}', (a, b)))(x[-1], y[-1])

plt.show()
