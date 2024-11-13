def save_text():

    global user_text
    if user_text == "":
        return

    try:
        f = open('writeups.txt', 'r')
    except FileNotFoundError:
        f = open('writeups.txt', 'w')
        f.write(user_text)
        user_text = ""
        return

    else:
        cont = f.read()
        if cont == "":
            text_to_write = user_text
        else:
            text_to_write = f'\n{user_text}'

        with open('writeups.txt', 'a') as f:
            f.write(text_to_write)
            user_text = ""
    finally:
        return
