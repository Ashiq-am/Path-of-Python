# importing modules
from tqdm import trange
from time import sleep

# creating loop
for i in trange(10, desc="loop "):
    # slowing the for loop
    sleep(0.1)
