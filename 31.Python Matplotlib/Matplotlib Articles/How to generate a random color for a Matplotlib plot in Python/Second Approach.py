import random as random
import matplotlib.pyplot as plt
import numpy as np

l = []
teams = ['Kolkata', 'Delhi', 'Mumbai', 'Punjab',
         'Hyderabad', 'Bangalore', 'Rajasthan', 'Chennai']

wincount = [2, 0, 6, 0, 1, 0, 1, 4]

plt.xlabel("Teams")
plt.ylabel("Winning Count")
plt.title("IPL RECORDS")

for i in range(0, len(teams) + 1):
    l.append(tuple(np.random.choice(range(0, 2), size=3)))

plt.bar(teams, wincount, color=l)
