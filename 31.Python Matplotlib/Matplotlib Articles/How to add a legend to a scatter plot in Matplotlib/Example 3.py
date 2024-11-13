# import required modules
import matplotlib.pyplot as plt

# adjust coordinates
x = [1,2,3,4,5]
y1 = [2,4,6,8,10]
y2 = [3,6,9,12,15]

# depict illustartion
plt.scatter(x, y1)
plt.scatter(x,y2)

# apply legend()
plt.legend(["x*2" , "x*3"], bbox_to_anchor = (1 , 1))
plt.show()
