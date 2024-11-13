# Python porgram to demonstrate
# social computing


from statistics import mean

# Estimation provided by various
# users
Estimates = [1000, 1010, 1223, 52223, 2411,
			322, 563, 1246, 1000, 2333, 4666, 2133]

Estimates.sort()

tv = int(0.1 * len(Estimates))

# Removing Underestimating value
Estimates = Estimates[tv:]

# Removing overestimating value
Estimates = Estimates[:len(Estimates)-tv]


print(mean(Estimates))
