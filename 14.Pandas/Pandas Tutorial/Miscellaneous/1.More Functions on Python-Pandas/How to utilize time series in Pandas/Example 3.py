# importing time delta module
from datetime import timedelta

# subtracting date from year 2027 to 2021
deltaresult = datetime(2027, 5, 7) - datetime(2021, 6, 24)

# display the result
print(deltaresult)

# to get days
print(deltaresult.days)

# to get seconds difference
print(deltaresult.seconds)
