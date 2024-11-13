# Specifications of Filter

# sampling frequency
f_sample = 3500

# pass band frequency
f_pass = 1050

# stop band frequency
f_stop = 600

# pass band ripple
fs = 0.5

# pass band freq in radian
wp = f_pass / (f_sample / 2)

# stop band freq in radian
ws = f_stop / (f_sample / 2)

# Sampling Time
Td = 1

# pass band ripple
g_pass = 1

# stop band attenuation
g_stop = 50
