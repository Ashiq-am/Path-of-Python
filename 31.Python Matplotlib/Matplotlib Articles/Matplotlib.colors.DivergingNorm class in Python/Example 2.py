import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.colors as colors

file = cbook.get_sample_data('topobathy.npz',
							asfileobj = False)

with np.load(file) as example:
	topo = example['topo']
	longi = example['longitude']
	latit = example['latitude']

figure, axes = plt.subplots(constrained_layout = True)

# creating a colormap that
# has land and ocean clearly
# delineated and of the
# same length (256 + 256)
undersea = plt.cm.terrain(np.linspace(0, 0.17, 256))
land = plt.cm.terrain(np.linspace(0.25, 1, 256))
every_colors = np.vstack((undersea, land))

terrain_map = colors.LinearSegmentedColormap.from_list('terrain_map',
													every_colors)

# the center is offset so that
# the land has more dynamic range
# while making the norm
diversity_norm = colors.DivergingNorm(vmin =-500,
									vcenter = 0,
									vmax = 4000)

pcm = axes.pcolormesh(longi, latit, topo,
					rasterized = True,
					norm = diversity_norm,
					cmap = terrain_map, )

axes.set_xlabel('Longitude $[^o E]$')
axes.set_ylabel('Latitude $[^o N]$')
axes.set_aspect(1 / np.cos(np.deg2rad(49)))

figure.colorbar(pcm, shrink = 0.6,
				extend ='both',
				label ='Elevation [m]')
plt.show()
