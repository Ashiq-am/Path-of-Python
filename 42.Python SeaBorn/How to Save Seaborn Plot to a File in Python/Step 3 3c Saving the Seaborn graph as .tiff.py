# code
# Install seaborn using pip install seaborn
# Import the seaborn package
import seaborn as sns

# load the inbuilt "penguins" dataset using
# seaborn inbuilt function load_dataset
data = sns.load_dataset("penguins")


scatter_plot = sns.scatterplot(
	x=data['bill_length_mm'], y=data['bill_depth_mm'], hue=data['sex'])

# use get_figure function and store the plot
# in a variable (scatter_fig)
scatter_fig = scatter_plot.get_figure()

# use savefig function to save the plot and give
# a desired name to the plot.
scatter_fig.savefig('scatterplot.tiff')

# this will store the plot in current working directory
