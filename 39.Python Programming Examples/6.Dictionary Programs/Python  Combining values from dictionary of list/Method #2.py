# Python code to combine every key value
# pair in every combinations

# Importing
import itertools

# Input Initialization
Input = {
    "Bool": ["True", "False"],
    "Data": ["Int", "Float", "Long Long"],
}

# using zip and product without sorting
Output = [[{key: value} for (key, value) in zip(Input, values)]
          for values in itertools.product(*Input.values())]

# Printing output
print(Output)
