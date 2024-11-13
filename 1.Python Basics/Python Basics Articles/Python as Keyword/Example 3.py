# Python code to demonstrait
# 'as' keyword

# Using alias with try statement
try:
    import maths as mt
except ImportError as err:
    print(err)


# Function showing alias functioning

def geek_Func():
    try:

        # With statement with geek alias
        with open('geek.txt') as geek:

            # reading text with aias
            geek_read = geek.read()

        # Printing our text
        print("Reading alias:")
        print(geek_read)
    except FileNotFoundError as err2:
        print('No file found')


geek_Func()
