def update_heatmap(frame, ax):
    ax.clear()
    sns.heatmap(data_frames[frame], ax=ax, cbar=True, annot=True)
