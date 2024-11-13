import matplotlib.pyplot as plt
import matplotlib as mpl

figure, axes = plt.subplots(figsize =(6, 1))
figure.subplots_adjust(bottom = 0.5)

color_map = mpl.cm.cool
normlizer = mpl.colors.Normalize(vmin = 0, vmax = 5)

figure.colorbar(mpl.cm.ScalarMappable(norm = normlizer,
			cmap = color_map),
			cax = axes, orientation ='horizontal',
			label ='Arbitary Units')
