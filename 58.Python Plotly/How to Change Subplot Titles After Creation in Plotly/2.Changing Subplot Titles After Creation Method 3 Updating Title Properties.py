# Update title properties
fig.layout.annotations[0].update(text="Custom Plot 1", font=dict(size=16, color="blue"), align="center")
fig.layout.annotations[1].update(text="Custom Plot 2", font=dict(size=14, color="green"), align="left")

# Display the updated figure
fig.show()
