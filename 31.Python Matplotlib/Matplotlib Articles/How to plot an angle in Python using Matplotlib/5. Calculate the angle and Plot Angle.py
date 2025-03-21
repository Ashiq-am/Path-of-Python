# import packages
import matplotlib.pyplot as plt
import numpy as np

# slope and intercepts
a1, b1 = (1/4), 1.0
a2, b2 = (3/4), 0.0

# The numpy.linspace() function returns
# number spaces evenly w.r.t interval
l = np.linspace(-6, 6, 100)

# use to create new figure
plt.figure(figsize=(8, 8))

# plotting
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.title('Plot an angle using Python')
plt.plot(l, l*a1+b1)
plt.plot(l, l*a2+b2)

# intersection point
x0 = (b2-b1)/(a1-a2)
y0 = a1*x0 + b1
plt.scatter(x0, y0, color='midnightblue')

# circle for angle
theta = np.linspace(0, 2*np.pi, 100)
r = 1.0
x1 = r * np.cos(theta) + x0
x2 = r * np.sin(theta) + y0
plt.plot(x1, x2, color='green', linestyle='dotted')


# intersection points
x_points = []
y_points = []

# Code for Intersecting points of circle with Straight Lines
def intersection_points(slope, intercept, x0, y0, radius):
	a = 1 + slope**2
	b = -2.0*x0 + 2*slope*(intercept - y0)
	c = x0**2 + (intercept-y0)**2 - radius**2

	# solving the quadratic equation:
	delta = b**2 - 4.0*a*c # b^2 - 4ac
	x1 = (-b + np.sqrt(delta)) / (2.0 * a)
	x2 = (-b - np.sqrt(delta)) / (2.0 * a)

	x_points.append(x1)
	x_points.append(x2)

	y1 = slope*x1 + intercept
	y2 = slope*x2 + intercept

	y_points.append(y1)
	y_points.append(y2)

	return None


# Finding the intersection points for line1 with circle
intersection_points(a1, b1, x0, y0, r)

# Finding the intersection points for line1 with circle
intersection_points(a2, b2, x0, y0, r)

# Here we plot Two ponts in order to find angle between them
plt.scatter(x_points[0], y_points[0], color='crimson')
plt.scatter(x_points[2], y_points[2], color='crimson')


# Naming the points.
plt.text(x_points[0], y_points[0], ' Point_P1', color='black')
plt.text(x_points[2], y_points[2], ' Point_P2', color='black')


# plot angle value

def get_angle(x, y, x0, y0, radius):

	base = x - x0
	hypotenuse = radius

	# calculating the angle for a intersection point
	# which is equal to the cosine inverse of (base / hypotenuse)
	theta = np.arccos(base / hypotenuse)

	if y-y0 < 0:
		theta = 2*np.pi - theta

	print('theta=', theta, ',theta in degree=', np.rad2deg(theta), '\n')

	return theta


theta_list = []

for i in range(len(x_points)):

	x = x_points[i]
	y = y_points[i]

	print('intersection point p{}'.format(i))
	theta_list.append(get_angle(x, y, x0, y0, r))

	# angle for intersection point1 ( here point p1 is taken)
p1 = theta_list[0]

# angle for intersection point2 ( here point p4 is taken)
p2 = theta_list[2]

# all the angles between the two intersection points
theta = np.linspace(p1, p2, 100)

# calculate the x and y points for
# each angle between the two intersection points
x1 = r * np.cos(theta) + x0
x2 = r * np.sin(theta) + y0

# plot the angle
plt.plot(x1, x2, color='black')

# Code to print the angle at the midpoint of the arc.
mid_angle = (p1 + p2) / 2.0

x_mid_angle = (r-0.5) * np.cos(mid_angle) + x0
y_mid_angle = (r-0.5) * np.sin(mid_angle) + y0

angle_in_degree = round(np.rad2deg(abs(p1-p2)), 1)

plt.text(x_mid_angle, y_mid_angle, angle_in_degree, fontsize=12)

# plotting the intersection points
plt.scatter(x_points[0], y_points[0], color='red')
plt.scatter(x_points[2], y_points[2], color='red')
plt.show()
