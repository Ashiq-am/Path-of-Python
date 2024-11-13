# Add counts as annotations
for i, count in enumerate(counts):
    ax.text(i, tips['total_bill'].max() + 2, f"Count: {count}",
            ha='center', size='medium', color='black', weight='semibold')
