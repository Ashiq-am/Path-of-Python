# importing modules
from tqdm import tnrange
from time import sleep

# creating loop
for i in tnrange(2, desc="loop 1"):

    # creating nested loop
    for j in tnrange(5, desc="loop 2"):
        # slowing the for loop
        sleep(0.2)
