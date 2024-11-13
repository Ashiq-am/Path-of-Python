import matplotlib.pyplot as plt

x_inp = input("Enter values of X array: ").split()
x = [int(i) for i in x_inp]

y1_inp = input("Enter values of Y1 array: ").split()
y1 = [int(i) for i in y1_inp]

y2_inp = input("Enter values of Y2 array: ").split()
y2 = [int(i) for i in y2_inp]

color = input("Enter color: ")

plt.fill_between(x, y1, y2, color=color)
plt.show()
