def concatenate_string(*args):
    string1 = args[0]
    string2 = args[1]

    def merge_string(string1, string2):
        return string1 + string2

    return merge_string(string1, string2)


def func():
    conc_obj = concatenate_string('Hello, ', 'George')
    print(conc_obj)


func()
