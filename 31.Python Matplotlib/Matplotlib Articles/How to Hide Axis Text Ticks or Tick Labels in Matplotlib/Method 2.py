import matplotlib.pyplot as plt

plt.plot([5, 10, 20], [20, 10, 50], color='g')

plt.xlabel("X Label")
plt.ylabel("Y Label")

# xticks color white
plt.xticks(color='w')

# yticks color white
plt.yticks(color='w')

plt.show()
