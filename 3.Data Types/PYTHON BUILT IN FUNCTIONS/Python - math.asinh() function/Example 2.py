# Python code to implement
# the aasinh()function
import math
import matplotlib.pyplot as plt

in_array = [-0.14159265, -0.57039399, -0.28559933,
            0.28559933, 0.57039399, 0.94159265]

out_array = []

for i in range(len(in_array)):
    out_array.append(math.asinh(in_array[i]))
    i += 1

print("Input_Array : \n", in_array)
print("\nOutput_Array : \n", out_array)

plt.plot(in_array, out_array, "go:")
plt.title("math.asinh()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
