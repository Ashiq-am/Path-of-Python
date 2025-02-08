import matplotlib.pyplot as plt
# Unicode character (Check)
uni_char = u"\u2717"  # Check Mark

plt.text(0.5, 0.5, uni_char, fontsize=50, ha='center', va='center')
plt.axis('on')
plt.show()