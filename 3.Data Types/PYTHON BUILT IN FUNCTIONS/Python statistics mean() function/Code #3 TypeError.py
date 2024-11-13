# Python3 code to demonstrate TypeError

# importing statistics module
from statistics import mean

# While using dictionaries, only keys are
# taken into consideration by mean()
dic = {"one":1, "three":3, "seven":7,
	"twenty":20, "nine":9, "six":6}

# Will raise TypeError
print(mean(dic))
