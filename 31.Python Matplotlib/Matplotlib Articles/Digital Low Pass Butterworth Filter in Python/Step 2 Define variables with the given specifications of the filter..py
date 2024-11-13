# Specifications of Filter

# sampling frequency
f_sample = 40000

# pass band frequency
f_pass = 4000

# stop band frequency
f_stop = 8000

# pass band ripple
fs = 0.5

# pass band freq in radian
wp = f_pass/(f_sample/2)

# stop band freq in radian
ws = f_stop/(f_sample/2)

# Sampling Time
Td = 1

# pass band ripple
g_pass = 0.5

# stop band attenuation
g_stop = 40
