# impoert required modules
import matplotlib.pyplot as plt

# adjust coordinates
x = [1,2,3,4,5]
y1 = [2,4,6,8,10]
y2 = [3,6,9,12,15]

# depict illustration
plt.scatter(x, y1)
plt.scatter(x,y2)

# appply legend()
plt.legend(["x*2" , "x*3"], ncol = 2 , loc = "lower right")
plt.show()
