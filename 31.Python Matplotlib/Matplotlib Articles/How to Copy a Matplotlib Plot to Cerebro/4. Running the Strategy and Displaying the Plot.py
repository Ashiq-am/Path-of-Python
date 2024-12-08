# Step 4: Generate Custom Portfolio Value Data for Matplotlib

portfolio_value = 100000 + np.cumsum(np.random.randn(days) * 100 + 50) # Example portfolio value

fig = cerebro.plot(style='candlestick')[0][0]
ax = fig.gca()

ax.plot(date_range, portfolio_value, label='Portfolio Value', color='orange', linewidth=2)
ax.legend(loc='upper left')

fig.savefig('combined_backtrader_plot.png')
plt.show()