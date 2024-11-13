# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

w = plt.get_plot_commands()

print("List of all of the plotting commands : ")
for i in w:
    print(i)
