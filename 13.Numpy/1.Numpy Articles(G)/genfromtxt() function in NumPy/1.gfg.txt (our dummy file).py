#importing numpy library
import numpy as np

#driver code
if __name__ == "__main__":
  data = np.genfromtxt("gfg.txt", dtype=str, encoding = None, delimiter=",")
  #displaying the data
  for i in data:
    print(i,end=" ")
