def concatenate_strings(str1, str2):
    if str1 and str2:
        return str1 + str2
    else:
        return None
result = concatenate_strings("Hello, ", "World!")
print(result + ", welcome!")  # This line raises TypeError
