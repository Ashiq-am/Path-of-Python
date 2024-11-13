fig, ax = init_heatmap()
anim = FuncAnimation(fig, update_heatmap, frames=num_frames, fargs=(ax,), interval=200)
