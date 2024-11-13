import matplotlib.pyplot as plt


w = 4
h = 3
d = 70

plt.figure(figsize=(w, h), dpi=d)

x = [1, 2, 4]
x_pos = 0.5
y_pos = 3

plt.text(x_pos, y_pos, "text on plot")
plt.plot(x)
plt.savefig("out.png")
