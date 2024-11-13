# Custom annotation function with color parameter
def annotate_diagonal(data, mask, ax, color='red'):
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if mask[i, j]:
                ax.text(j + 0.5, i + 0.5, f'{data[i, j]:.2f}',
                        ha='center', va='center', color=color)
