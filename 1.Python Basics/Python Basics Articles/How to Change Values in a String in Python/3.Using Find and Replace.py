import tokenize
from io import StringIO


def rename_variables(code, replacements):
    result = []
    with StringIO(code) as f:

        tokens = tokenize.generate_tokens(f.readline)
        for toktype, tokval, _, _, _ in tokens:
            if toktype == tokenize.NAME and tokval in replacements:
                new_name = replacements[tokval]

                if not new_name[0].isalpha() and new_name[0] != '_':
                    new_name = f'@{new_name}'

                result.append(new_name)
            else:
                result.append(tokval)

    return ''.join(result)


# function execution:
old_code = "x = 5\ny = x + 3\nprint(my_variable)"
replacements = {'x': 'z', 'y': 'w', 'my_variable': 'geeks_for_geeks'}

new_code = rename_variables(old_code, replacements)
print(new_code)
