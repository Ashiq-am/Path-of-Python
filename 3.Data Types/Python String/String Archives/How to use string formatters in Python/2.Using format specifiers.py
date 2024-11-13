# string
st = "This is a string"
print("String is %s" % (st))

# single character
ch = 'a'
print("Single character is %c" % (ch))

# integer
num = 45
print("The number is %d" % (num))

# float without specified precision
float1 = 34.521094
print("The float is %f" % (float1))

# float with precision
float2 = 7334.34819560
print("The float with precision is %.3f" % (float2))

# multiple specifiers in print()
# Hexa decimal representation
print("The hexadecimal form of %d is %x" % (num, num))

# octal representation
print("The octal form of %d is %o" % (num, num))

# exponential form
print("The exponential form of %f is %e" % (float1, float1))

# exponential form with appended space
print("The exponential form of %f is %10.3g" % (float2, float2))

# exponent less than -4 with appended space
float3 = 3.14
print("The exponential form of %.2f is %10.3g" % (float3, float3))
