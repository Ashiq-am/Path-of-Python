import datetime
import time
import sys

# Step 1: Import Necessary Modules
# datetime: for handling dates and times
# time: for managing delays
# sys: for output flushing

# Step 2: Define the Target New Year Date
cy = datetime.datetime.now().year
ny = datetime.datetime(cy + 1, 1, 1, 0, 0, 0)

# Step 3: Create the Countdown Loop
while True:
    # Step 4: Calculate the Remaining Time
    now = datetime.datetime.now()
    time = ny - now

    # Step 5: Extract Days, Hours, Minutes, and Seconds
    d = time.days
    h, remainder = divmod(time.seconds, 3600)
    m, s = divmod(remainder, 60)

    # Step 6: Display the Countdown Timer on the Same Line
    ctdown = f" New Year Countdown  | Time remaining: {d} Days, {h} Hours, {m} Minutes, {s} Seconds"

    # Print with carriage return and flush
    print("\r" + ctdown, end='', flush=True)

    # Step 7: Check for Countdown Completion
    if time_left.total_seconds() <= 0:
        print("\n Happy New Year! ")
        break

    # Step 8: Pause the Loop for One Second
    time.sleep(1)
