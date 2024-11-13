# Python code to demonstrait
# 'as' keyword

def geek_Func():
    # With statement with geek alias
    with open('sample.txt') as geek:
        # reading text with aias
        geek_read = geek.read()

    # Printing our text
    print("Text read with alias:")
    print(geek_read)


geek_Func()
