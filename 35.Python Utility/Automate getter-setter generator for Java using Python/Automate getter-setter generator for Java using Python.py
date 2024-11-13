# Function to print getter and setter methods
# for variables according to Java
def print_getter_setter(variables, dataypes):
    # List to store getVariable
    getters = []

    # List to store setVariable
    setters = []

    # Iterate for every variable
    for var in variables:
        # Prepend "get" in every variable and change
        # the first character to uppercase
        getter = "get" + var[0].capitalize() + var[1:]
        getters.append(getter)

        # Prepend "set" in every variable and change
        # the first character to uppercase
        setter = "set" + var[0].capitalize() + var[1:]
        setters.append(setter)

    for i in range(len(variables)):
        # Print the getter method
        print("public " + datatypes[i] + " " + getters[i] +
              "() {\n\treturn " + variables[i] + ";\n}\n")

        # Print the setter method
        print("public void " + setters[i] + "(" + datatypes[i] +
              " " + variables[i] + ") {\n\tthis." + variables[i] +
              " = " + variables[i] + ";\n}\n")

    # Driver function


if __name__ == "__main__":
    # The list of variables
    variables = ["abc", "empId", "GFG", "x"]

    # And the list of the variables's corresponding
    # datatypes
    datatypes = ["int", "float", "double", "String"]

    print_getter_setter(variables, datatypes)
