def init_heatmap():
    fig, ax = plt.subplots()
    sns.heatmap(data_frames[0], ax=ax, cbar=True, annot=True)
    return fig, ax
