# Python3 code to generate Harmonic Progression
# and calculate the sum of the progression.
import math

# Function that generates the harmonic
# progression and calculates the sum of
# its elements by iterating.
n = 5
AP = [0] * (n + 5)


def generateAP(a, d, n):
    sum = 0
    for i in range(1, n + 1):

        # HP = 1/AP
        # In AP, ith term is calculated
        # by a+(i-1)d;
        AP[i] = (a + (i - 1) * d)

        # Calculating the sum.
        sum += float(1) / float((a + (i - 1) * d))
    return sum

# Function that uses riemann sum method to calculate
# the approximate sum of HP in O(1) time complexity


def sumApproximation(a, d, n):

    return math.log((2 * a + (2 * n - 1) * d) /
                    (2 * a - d)) / d


# Driver Code
a = 12
d = 12
#n = 5;

# Generating AP from the above data
sum = generateAP(a, d, n)

# Generating HP from the generated AP
print("Harmonic Progression :")
for i in range(1, n + 1):
    print("1 /", AP[i], end=" ")
print("")
str1 = ""
str1 = str1 + str(sum)
str1 = str1[0:4]

print("Sum of the generated harmonic",
      "progression :", str1)
sum = sumApproximation(a, d, n)

str1 = ""
str1 = str1 + str(sum)
str1 = str1[0:4]
print("Sum of the generated harmonic",
      "progression using approximation :", str1)
