import functools

import count as count

with open("test1.txt") as file:
    file_char = functools.partial(file.read, 1)

    for char in iter(file_char, " "):

        if char == " ":
            count += 1

    print("count: ", count)
