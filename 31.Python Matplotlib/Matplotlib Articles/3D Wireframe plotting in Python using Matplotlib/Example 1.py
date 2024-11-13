# importing modules
from mpl_toolkits.mplot3d import axes3d
from matplotlib import pyplot

# creating the visualiztion
fig = pyplot.figure()
wf = fig.add_subplot(111, projection='3d')
x, y, z = axes3d.get_test_data(0.05)
wf.plot_wireframe(x,y,z, rstride=2,
				cstride=2,color='green')

# displaying the visualization
wf.set_title('Example 1')
pyplot.show()
