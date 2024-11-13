import random as random
import matplotlib.pyplot as plt

teams = ['Kolkata', 'Delhi', 'Mumbai', 'Punjab',
		'Hyderabad', 'Bangalore', 'Rajasthan', 'Chennai']

wincount = [2, 0, 6, 0, 1, 0, 1, 4]

r = random.random()
b = random.random()
g = random.random()

color = (r, g, b)

plt.xlabel("Teams")
plt.ylabel("Winning Count")
plt.title("IPL RECORDS")
plt.plot(teams, wincount, c=color)
