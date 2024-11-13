def concatenate_string(*args):
    string1 = args[0]
    string2 = args[1]

    def merge_string(string1, string2):
        return string1 + string2  # string merge

    # executes merge_string and return the result
    return merge_string(string1, string2)


def function_call(function):
    string1 = 'Hello, '
    string2 = 'George'
    return function(string1, string2)


# passing function as argument
print(function_call(concatenate_string))
