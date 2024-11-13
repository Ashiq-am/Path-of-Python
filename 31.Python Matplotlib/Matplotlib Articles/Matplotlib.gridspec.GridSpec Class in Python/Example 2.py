import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


fig = plt.figure(figsize =([7, 4]))

gs = gridspec.GridSpec(2, 6)
gs.update(wspace = 1.5, hspace = 0.3)

ax1 = plt.subplot(gs[0, :2])
ax1.set_ylabel('ylabel', labelpad = 0, fontsize = 12)

ax2 = plt.subplot(gs[0, 2:4])
ax2.set_ylabel('ylabel', labelpad = 0, fontsize = 12)

ax3 = plt.subplot(gs[0, 4:6])
ax3.set_ylabel('ylabel', labelpad = 0, fontsize = 12)

ax4 = plt.subplot(gs[1, 1:3])
ax4.set_ylabel('ylabel', labelpad = 0, fontsize = 12)

ax5 = plt.subplot(gs[1, 3:5])
ax5.set_ylabel('ylabel', labelpad = 0, fontsize = 12)

plt.show()
