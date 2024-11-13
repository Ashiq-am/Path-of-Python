import textwrap

def example_function():
    multiline_string = textwrap.dedent("""\
        This is a
        multiline string inside a function.
        """)
    print(multiline_string)
