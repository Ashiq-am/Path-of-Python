# Import required module
from threading import *


# Extending Thread class
class Mythread(Thread):

    # Target function for thread
    def run(self):
        for i in range(10):
            print('Child Thread')

        # Driver Code


# Creating thread class object
t = Mythread()

# Execution of target function
t.start()

# Executed by main thread
for i in range(10):
    print('Main Thread')
