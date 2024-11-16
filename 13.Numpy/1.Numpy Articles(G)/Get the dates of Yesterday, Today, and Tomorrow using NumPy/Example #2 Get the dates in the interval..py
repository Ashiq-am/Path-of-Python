import numpy as np

# for today
today = np.datetime64('today', 'D')
print("Today: ", today)

# for before_2_day
before_2_day = np.datetime64('today', 'D') - np.timedelta64(2, 'D')
print("before_2_day : ", before_2_day)

# for after_2_day
after_2_day = np.datetime64('today', 'D') + np.timedelta64(2, 'D')

print("after_2_day :", after_2_day)
