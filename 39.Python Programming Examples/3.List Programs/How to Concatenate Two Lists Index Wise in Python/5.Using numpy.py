import numpy as np

#Converting list into numpay array
list1 = np.array(["gf", "i", "be"])
list2 = np.array(["g", "s", "st"])

#applying the char.add() function on the arrays
ans = np.char.add(list1, list2).tolist()

#dispalying the output
print(ans)
