import matplotlib.pyplot as plt
import time

plt.figure()
plt.plot([1, 2, 3])
plt.show(block=False)
time.sleep(10)  # Keep the figure open for 1o seconds
plt.close()    # Close the figure after 10 seconds