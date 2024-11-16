# Specifying multiple dates for the vertical lines
event_dates = ['2023-02-01', '2023-02-15', '2023-03-01']
ax = df.plot()

# Adding multiple vertical lines
for event_date in event_dates:
    plt.axvline(x=event_date, color='green', linestyle='--', linewidth=1)

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Plot with Multiple Vertical Lines')
plt.show()
